#!/usr/bin/env python3

'''
Usage:
  list-timelapses <dir>
'''

import os
from itertools import groupby
from docopt import docopt

interval = 5.0

def list_dir(dir):
	for root, dir, files in os.walk(dir):
		for file in files:
			yield os.path.join(root, file)

def partition(iter, fn):
	current_group = []
	prev = None
	for v in iter:
		if prev is not None and fn(prev, v):
			yield current_group
			current_group = []
		current_group.append(v)
		prev = v
	if len(current_group) > 0:
		yield current_group
	
def list_timelapses(dir):
	pics = ((os.path.getmtime(f), f) for f in list_dir(dir) if f.lower().endswith('.jpg'))
	pics = sorted(pics)
	groups = partition(pics, lambda a,b: b[0] - a[0] > interval)
	groups = [[f for _, f in g] for g in groups if len(g) > 5]
	for i, g in enumerate(groups):
		with open(str(i), 'w') as f:
			for x in g:
				f.write(x + '\n')

if __name__ == '__main__':
	args = docopt(__doc__)
	list_timelapses(os.path.abspath(args['<dir>']))
