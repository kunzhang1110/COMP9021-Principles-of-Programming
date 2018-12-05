from general_tree import *
import sys

fh = open("tree.txt", 'r')
value_level = []
for line in fh:
    line = line.rstrip()
    level = 0
    line_string = ""
    for c in line:
        if c == '\t':
            level += 1
        else:
             line_string += c
    if line_string:
        value_level.append((int(line_string), level))

value_level.reverse()

def build_tree(all_info):
    current_value, current_level = all_info.pop()
    tree = GeneralTree(current_value)
    while all_info:
        next_level = all_info[-1][1]
        if next_level == current_level + 1:
            tree.children.append(build_tree(all_info))
        elif next_level > current_level + 1:
            print("Error")
            sys.exit()
        else:
            return tree
    return tree

def print_tree(tree, level):
    print('\t'*level, tree.value)
    for child in tree.children:
        print_tree(child, level+1)
    return None

lab_10_tree = build_tree(value_level)
print_tree(lab_10_tree, 0)