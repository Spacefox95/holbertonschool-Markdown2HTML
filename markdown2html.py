#!/usr/bin/python3

""" Script to translate Markdow in HTML """

import sys
import os.path

if len(sys.argv) != 3 :
	print("Usage: ./markdown2html.py README.md README.html")
	exit(1)
mdfile = sys.argv[1]
htmlfile = sys.argv[2]

if not os.path.isfile(mdfile):
	print("Missing {}".format(mdfile))
	exit(1)
else:
	print('')
	with open(mdfile, 'r') as f:
			content = f.read()
			with open(htmlfile, 'w') as file:
				file.write(content)
	exit(0)
