#!/usr/bin/env python3

'''
Usage:
  assemble-timelapse <list-of-files>
'''

import os
from subprocess import check_call
import tempfile
from docopt import docopt

def assemble(input):
	with tempfile.TemporaryDirectory() as dir:
		with open(input, 'r') as f:
			for i, filename in enumerate(f):
				os.symlink(filename.strip(), os.path.join(dir, '%04d.jpg' % i))
		check_call(['ls', '-l', dir])
		check_call([
			'ffmpeg',
			'-i', os.path.join(dir, '%04d.jpg'),
			'-r', '24',
			'-vcodec', 'libx264',
			'-s', '1620x1080',
			'-b:v', '20000k',
			'-pix_fmt', 'yuv420p',
			input+'.mp4'
		])


if __name__ == '__main__':
	args = docopt(__doc__)
	assemble(args['<list-of-files>'])
