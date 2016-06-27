#!/usr/bin/env python3

# RAW deflickering script
# Copyright (2012) a1ex. License: GPL.

from __future__ import division
import os, sys, re, time, datetime, subprocess, shlex
from multiprocessing import Pool
from math import *
from statistics import median
from scipy.signal import detrend


XMP_TEMPLATE = '''<x:xmpmeta xmlns:x="adobe:ns:meta/" x:xmptk="Magic Lantern">
 <rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
  <rdf:Description rdf:about=""
    xmlns:dc="http://purl.org/dc/elements/1.1/"
    xmlns:photoshop="http://ns.adobe.com/photoshop/1.0/"
    xmlns:crs="http://ns.adobe.com/camera-raw-settings/1.0/"
   photoshop:DateCreated="2050-01-01T00:00:00:00"
   photoshop:EmbeddedXMPDigest=""
   crs:ProcessVersion="6.7"
   crs:Exposure2012="%s">
   <dc:subject>
    <rdf:Bag>
     <rdf:li>ML Post-Deflicker</rdf:li>
    </rdf:Bag>
   </dc:subject>
  </rdf:Description>
 </rdf:RDF>
</x:xmpmeta>
'''


def progress(x, interval=1):
    global _progress_first_time, _progress_last_time, _progress_message, _progress_interval
    
    try:
        p = float(x)
        init = False
    except:
        init = True
        
    if init:
        _progress_message = x
        _progress_last_time = time.time()
        _progress_first_time = time.time()
        _progress_interval = interval
    elif x:
        if time.time() - _progress_last_time > _progress_interval:
            print("%s [%d%% done, ETA %s]..." % (_progress_message, int(100*p), datetime.timedelta(seconds = round((1-p)/p*(time.time()-_progress_first_time)))), file=sys.stderr)
            _progress_last_time = time.time()


def get_median(file):
    print(file)
    cmd1 = "dcraw -c -d -4 -o 0 '%s'" % file
    cmd2 = "convert - -type Grayscale -scale 500x500 -format %c histogram:info:-"
    p1 = subprocess.Popen(shlex.split(cmd1), stdout=subprocess.PIPE)
    p2 = subprocess.Popen(shlex.split(cmd2), stdin=p1.stdout, stdout=subprocess.PIPE)
    out = p2.communicate()[0]
    lines = out.decode('utf8').split("\n")
    X = []
    for l in lines[1:]:
        p1 = l.find("(")
        if p1 > 0:
            p2 = l.find(",", p1)
            level = int(l[p1+1:p2])
            count = int(l[:p1-2])
            X += [level]*count
    m = log2(median(X))
    return m


if __name__ == '__main__':
    print("Analyzing RAW exposures...")
    files = sorted((f for f in os.listdir('.') if f.endswith('.CR2')))
    with Pool(5) as pool:
        M = pool.map(get_median, files)

    E = [(M[0] - m) for m in M]
    E = detrend(E, type='constant')

    print("Writing XMP files...")
    for filename, ec in zip(files, E):
        xmp = XMP_TEMPLATE % (ec,)
        with open(os.path.splitext(filename)[0] + '.xmp', 'w') as f:
            f.write(xmp)

