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
        paragraph_content = []
        in_ul = False
        in_ol = False
        in_p = False

        for line in lines:
            stripped_line = line.strip()

            # Heading Levels
            if stripped_line.startswith('#'):
                h_counter = len(stripped_line.split(' ')[0])
                if h_counter <= 6:
                    h_text = stripped_line[h_counter:].strip()
                    html_content += f'<h{h_counter}>{h_text}</h{h_counter}>\n'
                continue

            # Unordered List
            if stripped_line.startswith('- '):
                if in_p:
                    html_content += f"<p>\n{''.join(paragraph_content)}\n</p>\n"
                    paragraph_content = []
                    in_p = False
                if not in_ul:
                    html_content += '<ul>\n'
                    in_ul = True

                clean_list = stripped_line[2:].strip()
                html_content += f'<li>{clean_list}</li>\n'
                continue

            # Ordered List
            if stripped_line.startswith('* '):
                if in_p:
                    html_content += f"<p>\n{''.join(paragraph_content)}\n</p>\n"
                    paragraph_content = []
                    in_p = False

                if not in_ol:
                    html_content += '<ol>\n'
                    in_ol = True

                order_list = stripped_line[2:].strip()
                html_content += f'<li>{order_list}</li>\n'
                continue

            # Paragraph
            if stripped_line:
                if in_ul:
                    html_content += "</ul>\n"
                    in_ul = False
                if in_ol:
                    html_content += "</ol>\n"
                    in_ol = False
                paragraph_content.append(stripped_line + '\n<br />\n')
                in_p = True
            
            else:
                if in_p:
                    html_content += f"<p>\n{''.join(paragraph_content)}\n</p>\n"
                    paragraph_content = []
                    in_p = False

        if in_ul:
            html_content += '</ul>\n'
        if in_ol:
            html_content += '</ol>\n'
        if in_p:
            html_content += f"<p>\n{''.join(paragraph_content)}\n</p>\n"

        with open(htmlfile, 'w') as file:
            file.write(html_content)

    except Exception as e:
        sys.stderr.write(f'Error: {e}')
        sys.exit(1)


if __name__ == "__main__":
    main()
