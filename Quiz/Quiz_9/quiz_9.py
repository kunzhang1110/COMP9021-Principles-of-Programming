# Randomly generates a binary search tree whose number of nodes
# is determined by user input, with labels ranging between 0 and 999,999,
# displays it, and outputs the maximum difference between consecutive leaves.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randrange
from binary_tree import *

# Possibly define some functions

def max_diff_in_consecutive_leaves(tree):
    all_consecutive_leaves = []

    def get_leaves(current_node):
        if current_node.value:
       #     print(current_node.value, current_node.left_node.value, current_node.right_node.value)
            if (not current_node.left_node.value) and (not current_node.right_node.value): # then it is a leaf
                all_consecutive_leaves.append(current_node.value)
                return
        else:
                return
        get_leaves(current_node.left_node)
        get_leaves(current_node.right_node)

    get_leaves(tree)
    number_of_leaves = len(all_consecutive_leaves)
    max_dif = 0
    if number_of_leaves < 2:
        return max_dif
    for i in range(number_of_leaves -1):
        dif = abs(all_consecutive_leaves[i] - all_consecutive_leaves[i+1])
        if dif > max_dif:
            max_dif = dif
    return max_dif


provided_input = input('Enter two integers, the second one being positive: ')
provided_input = provided_input.split()
if len(provided_input) != 2:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    seed_arg = int(provided_input[0])
    nb_of_nodes = int(provided_input[1])
    if nb_of_nodes < 0:
        raise ValueError
except:
    print('Incorrect input, giving up.')
    sys.exit()

seed(seed_arg)
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = randrange(1000000)
    tree.insert_in_bst(datum)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
print('The maximum difference between consecutive leaves is: ', end = '')
print(max_diff_in_consecutive_leaves(tree))
