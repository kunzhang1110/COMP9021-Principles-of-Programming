import re
s = 'EE-225 '
rm = re.match(r'[\S\s]+\S\s\Z',s)
print(rm.group())