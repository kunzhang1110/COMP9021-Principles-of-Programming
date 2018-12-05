# check it represents a tree
# all test files contain 2 non-blank lines
import re
import sys


def print_leading_space(num):
    print("Wrong number of leading spaces on nonblank line {}".format(num+1))
    sys.exit()

file_name = "tree_2.txt"
fh = open(file_name, 'r', encoding="ascii")

line_match_space = []
line_match_label = []

for line in fh:
    line_match = re.match(r'([ ]*)(\S[\S\s]*\S|\S)', line)  # fine pattern
    if line_match:
        line_match_space.append(line_match.group(1))
        line_match_label.append( line_match.group(2)) # (space, label)

# check if the root is the first element

all_space_len = [len(l) for l in line_match_space]


# find out x and y value
value_x = all_space_len[0]
value_y = all_space_len[1] - all_space_len[0]

# find out all wrong leading spaces
all_level = []
previous_level = 0
for n in range(len(all_space_len)):
    level, rem = divmod(all_space_len[n]-value_x,  value_y)
    if all_space_len[n] <= all_space_len[0] and n > 0:
        print_leading_space(n)
    if rem:
        print_leading_space(n)
    if level - previous_level > 1:
        print_leading_space(n)
    previous_level = level
    all_level.append(level)
all_level_label = list(zip(all_level, line_match_label))
print(all_level_label)
fh.close()
tex_string = """\documentclass[10pt]{article}
\\usepackage{tikz}
\\usetikzlibrary{shapes}
\\pagestyle{empty}\n
\\begin{document}\n
\\begin{center}
\\begin{tikzpicture}\n"""


# all_level_label (level, label)
space = "     "
for i in range(len(all_level_label)):
    if all_level_label[i][1] == '\x0e':
        label_name = ''
    elif all_level_label[i][1] == '\x05':
        label_name = '[fill=none] {edge from parent[draw=none]'
    else:
        label_name = '{node ' + '{' + all_level_label[i][1] + '}'

    if i == 0:
        tex_string += '\\' + 'node ' + '{' + all_level_label[i][1] + '}'
    else:
        if i != len(all_level_label) - 1:
            level_diff = all_level_label[i+1][0] - all_level_label[i][0]
        else:
            level_diff = - all_level_label[i][0] + 1
        if level_diff == 1:
            tex_string += '\n' + space*all_level_label[i][0] + 'child ' + label_name
        if level_diff == 0:
            tex_string += '\n' + space*all_level_label[i][0] + 'child ' + label_name + '}'
        if level_diff < 0:
            tex_string += '\n' + space*all_level_label[i][0] + 'child ' + label_name + '}' + '\n'
            for j in range(abs(level_diff)):
                tex_string += space*(all_level_label[i][0] - j -1) + '}'
                if j != abs(level_diff)-1:
                    tex_string += '\n'
tex_string += """;
\end{tikzpicture}
\end{center}

\end{document}"""



fw = open('test.tex', 'w')
fw.write(tex_string)