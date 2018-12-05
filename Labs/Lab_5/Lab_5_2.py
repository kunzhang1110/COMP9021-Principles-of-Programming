import re

full_title_pattern = re.compile(r'title=[^>]*>([^<>]*)</a></h3>')
title_next_line_pattern = re.compile(r'[^">]*>([^<>]*)\n$')
tag_next_line_pattern = re.compile(r'^</a></h3>')

with open('SMH.txt', 'r', encoding="UTF-8") as file:
    line = file.readline()
    for next_line in file:
        full_match = re.search(full_title_pattern, line)
        if full_match:
            print(full_match.group(1))
        else:
            next_match = re.search(title_next_line_pattern, line)
            if next_match:
                tag_match = re.search(tag_next_line_pattern, next_line)
                if tag_match:
                    print(next_match.group(1))
        line = next_line
