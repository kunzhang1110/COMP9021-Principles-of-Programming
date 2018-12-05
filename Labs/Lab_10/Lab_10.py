import sys
from general_tree import *

file_handle = open('tree.txt', 'r')

all_line_level = []
for line in file_handle:
    level = 0
    stripped_line = line.rstrip()
    if stripped_line:
        for c in stripped_line:
            if c == '\t':
                level += 1
            else:
                all_line_level.append((level, int(line.strip())))
                break

print(all_line_level)
all_answer = []

for i in range(len(all_line_level)):
    current_level, current_value = all_line_level[i]
    some_answer = []
    for j in range(i+1, len(all_line_level)):
        some_level, some_value = all_line_level[j]
        if some_level <= current_level:
            break
        if some_level == current_level + 1:
            some_answer.append(some_value)
    if some_answer:
        # tree = GeneralTree(current_value)
        # for t in some_answer:
        #     tree.children.append(GeneralTree(t))
        all_answer.append((current_value, some_answer))

def _build_tree(parent):
    tree = GeneralTree(parent)
    for p, cl in all_answer:
        if parent == p:
            children = cl
            break
    print(parent, children)
    for child in children:
        if child in all_parent:
            all_parent.remove(child)
            tree.children.append(_build_tree(child))
        else:
            tree.children.append(GeneralTree(child))
    return tree

def print_out(tree):
    _print_out(tree, 0)


def _print_out(tree, level):
    print('\t' * level, end = '')
    print(tree.value)
    for subtree in tree.children:
        _print_out(subtree, level + 1)


all_parent = [p for p,t in all_answer]
print(all_parent)
print(all_answer)
whole_tree = _build_tree(all_parent[0])
print_out(whole_tree)

