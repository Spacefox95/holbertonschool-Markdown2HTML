#!/usr/bin/python3

""" Script to translate Markdow in HTML """

import sys
import os.path


if len(sys.argv) != 3 :
	sys.stderr.write('Usage: ./markdown2html.py README.md README.html')
	sys.exit(1)
mdfile = sys.argv[1]
htmlfile = sys.argv[2]

if not os.path.isfile(mdfile):
	sys.stderr.write("Missing {}".format(mdfile))
	sys.exit(1)
else:
	print('')
	sys.exit(0)
