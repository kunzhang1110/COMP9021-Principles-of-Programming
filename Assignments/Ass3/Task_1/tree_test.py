# check it represents a tree
# all test files contain 2 non-blank lines
import re
import sys


def print_leading_space(num):
    print("Wrong number of leading spaces on nonblank line {}".format(num+1))
    sys.exit()

file_name = "wrong_2.txt"
fh = open(file_name, 'r', encoding="ascii")

line_match_all = []
line_match_label = []

for line in fh:
    line_match = re.match(r'([ ]*)(\S[\S\s]*\S|\S)', line)  # fine pattern
    if line_match:
        line_match_all.append((line_match.group(1), line_match.group(2))) # (space, label)

# check if the root is the first element

all_space_len = [len(s) for s, l in line_match_all]


# find out x and y value
value_x = all_space_len[0]
value_y = all_space_len[1] - all_space_len[0]

# find out all wrong leading spaces
all_level = []
previous_level = 0
for n in range(len(all_space_len)):
    level, rem = divmod(all_space_len[n]-value_x,  value_y)
    print(level,rem)
    if all_space_len[n] <= all_space_len[0] and n > 0:
         print_leading_space(n)
    if rem:
         print_leading_space(n)
    if level - previous_level > 1:
         print_leading_space(n)
    previous_level = level
    all_level.append(level)
print(all_level)


