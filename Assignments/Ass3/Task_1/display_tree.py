import sys
import re


def check_file_name(fn):
    # check file name ends with .txt
    if fn[-4:] == ".txt":
        return True
    return False


def check_grow_direction(gd):
    # grow direction should be either down, up, left, right or empty
    if gd in ["down", "up", "left", "right", ""]:
        return True
    return False


def check_node_style(gd):
    # node style should be either rectangle, circle, ellipse or empty
    if gd in ["rectangle", "circle", "ellipse", ""]:
        return True
    return False


def print_invocation():
    print("Incorrect invocation")
    sys.exit()


def print_leading_space(num):
    print("Wrong number of leading spaces on nonblank line {}".format(num+1))
    sys.exit()

input_args = sys.argv[1:]

grow_direction = ""
node_style = ""

if len(input_args) not in [1, 3, 5]:
    print_invocation()
    # Check file name

opt_args = list(zip(input_args[:-1:2], input_args[1:-1:2]))

# parsing inputs
for opt, arg in opt_args:
    if opt == "-nodestyle":
        node_style = arg
    elif opt == "-grow":
        grow_direction = arg
    else:
        print_invocation()

if check_grow_direction(grow_direction) and check_node_style(node_style):
    pass
else:
    print_invocation()

file_name = input_args[-1]
if not check_file_name(file_name):
        print_invocation()
try:
    fh = open(file_name, 'r')
except FileNotFoundError:
    print("No file named {} in current directory".format(file_name))
    sys.exit()

line_match_space = []
line_match_label = []

for line in fh:
    line_match = re.match(r'([ ]*)(\S[\S\s]*\S|\S)', line)  # fine pattern
    if line_match:
        line_match_space.append(line_match.group(1))
        line_match_label.append( line_match.group(2))  # (space, label)

# check if the root is the first element
all_space_len = [len(l) for l in line_match_space]


# find out x and y value
value_x = all_space_len[0]
value_y = all_space_len[1] - all_space_len[0]

# find out all wrong leading spaces
all_level = []
previous_level = 0
for n in range(len(all_space_len)):
    level, rem = divmod(all_space_len[n]-value_x,  value_y)     # get level and remainder
    if all_space_len[n] <= all_space_len[0] and n > 0:
        print_leading_space(n)
    if rem:                         # remainder determines space number
        print_leading_space(n)
    if level - previous_level > 1:  # if it is next level print leading space
        print_leading_space(n)
    previous_level = level
    all_level.append(level)
all_level_label = list(zip(all_level, line_match_label))        # all labels and their levels
#print(all_level_label)
fh.close()          # end read file

# header text
tex_string = """\documentclass[10pt]{article}
\\usepackage{tikz}
\\usetikzlibrary{shapes}
\\pagestyle{empty}\n
\\begin{document}\n
\\begin{center}
\\begin{tikzpicture}\n"""
if grow_direction:      # direction text
    tex_string += '[grow\'='+ grow_direction + ']\n'
if node_style:
    tex_string += '\\tikzstyle{every node}=[' + node_style+ ',draw]\n'

# all_level_label (level, label)
space = "    "
for i in range(len(all_level_label)):
    special_head = ' '
    if all_level_label[i][1] == '\x0e':         # emtpy label text
        label_name = ''
    elif all_level_label[i][1] == '\x05':       # fill none label text
        label_name = 'edge from parent[draw=none]'
        special_head = '[fill=none] '
    else:   # normal label text
        label_name = 'node ' + '{' + all_level_label[i][1] + '}'

    if i == 0:  # for the first node
        tex_string += '\\' + 'node ' + '{' + all_level_label[i][1] + '}'
    else:   # for all other node
        if i != len(all_level_label) - 1:   # calculate level difference
            level_diff = all_level_label[i+1][0] - all_level_label[i][0]
        else:
            level_diff = - all_level_label[i][0] + 1
        tex_string += '\n' + space*all_level_label[i][0] + 'child'  # child text
        if level_diff == 1:     # if positive (has to be 1) level difference
            tex_string += special_head + '{'  + label_name
        if level_diff == 0:     # if the same level
            tex_string += special_head + '{' + label_name + '}'
        if level_diff < 0:      # if negative level difference
            if all_level_label[i][1] == '\x0e':
                tex_string += label_name + '\n'
            else:   # print label
                tex_string += special_head + '{' + label_name + '}' + '\n'
            for j in range(abs(level_diff)):  # print empty lines
                tex_string += space*(all_level_label[i][0] - j -1) + '}'
                if j != abs(level_diff)-1:
                    tex_string += '\n'
# end text
tex_string += """;
\end{tikzpicture}
\end{center}

\end{document}"""

# write everything to new tex file
new_file_name = file_name[:-4] + '.tex'
fw = open(new_file_name, 'w')
fw.write(tex_string)