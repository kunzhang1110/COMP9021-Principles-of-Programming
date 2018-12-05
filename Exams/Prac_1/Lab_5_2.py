# Extract info from HTML

import re

fh = open("Lab_5_2_SMH.txt", 'r', encoding='utf-8')
pattern_1 = r'title=[^>]*>([^<]*)</a></h3>'
pattern_2 = r'">([^<]*)'

line = fh.readline()
all_output = []
for next_line in fh:
    if re.search(pattern_1, line):
        print(re.search(pattern_1, line).group(1))
        all_output.append(re.search(pattern_1, line).group(1).strip())
    elif re.match('</a></h3>', next_line):
        print(re.search(pattern_2, line).group(1))
        all_output.append(re.search(pattern_2, line).group(1).strip())
    line = next_line

fh.close()

fs = open("Lab_5_my_output.txt", 'w')
for l in all_output:
    l += '\n'
    fs.write(l)