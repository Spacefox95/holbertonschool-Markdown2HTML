#!/usr/bin/python3

""" Script to translate Markdow in HTML """

import sys
import os.path


def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)
    mdfile = sys.argv[1]
    htmlfile = sys.argv[2]

    if not os.path.isfile(mdfile):
        sys.stderr.write("Missing {}\n".format(mdfile))
        sys.exit(1)
    try:
        with open(mdfile, 'r') as md_content:
            lines = md_content.readlines()
        html_content = ''
        for line in lines:
            stripped_line = line.strip()
            if stripped_line.startswith('#'):
                h_counter = len(stripped_line.split(' ')[0])
                if h_counter <= 6:
                    h_text = stripped_line[h_counter:].strip()
                    html_content += f'<h{h_counter}>{h_text}</h{h_counter}>\n'
                else:
                    html_content += line
            else:
                html_content += line
        with open(htmlfile, 'w') as file:
            file.write(html_content)
    except Exception as e:
        sys.stderr.write(f'Error: {e}')
        sys.exit(1)


if __name__ == "__main__":
    main()
