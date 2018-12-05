import re

with open('SMH.txt', 'r', encoding="utf-8") as f:
    line = f.readline()
    for nextline in f:
        if re.search(r'</a></h3>',nextline) and re.search(r'">([^<]*)$', line):
            print(re.search(r'">([^<]*)$', line).group(1))
        elif re.search(r'title=[^>]([^<]*)</a></h3>',line):
            print(re.search(r'title=[^>]*>([^<]*)</a></h3>',line).group(1))
        line = nextline
