from general_tree import *
import sys

fh = open('tree.txt', 'r')

all_tree_level = []
for line in fh:
    line = line.rstrip()
    level = 0
    for i in range(len(line)):
        if line[i] == '\t':
            level+=1
        else:
            all_tree_level.append((int(line[i:]), level))
            break

all_tree_level.reverse()
print(all_tree_level)

def build_tree(all_tree_level):
    current_value, current_level = all_tree_level.pop()
    tree = GeneralTree(current_value)
    while all_tree_level:
        next_value, next_level = all_tree_level[-1]
        if next_level == current_level + 1:
            tree.children.append(build_tree(all_tree_level))
        elif next_level > current_level + 1:
            print("Error")
            sys.exit()
        else:  # next < current
            return tree
    return tree

def print_tree(tree, level):
    print("\t"*level, tree.value)
    for child in tree.children:
        print_tree(child, level+1)

root = build_tree(all_tree_level)
print_tree(root, 0)
