#!/usr/bin/python3

""" Script to translate Markdow in HTML """

import sys
import os.path

if len(sys.argv) != 3 :
	sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
	sys.exit(1)
mdfile = sys.argv[1]
htmlfile = sys.argv[2]

if not os.path.isfile(mdfile):
	sys.stderr.write("Missing {}\n".format(mdfile))
	sys.exit(1)
else:
	with open(mdfile, 'r') as f:
			content = f.read()
			with open(htmlfile, 'w') as file:
				file.write(content)
	sys.exit(0)
