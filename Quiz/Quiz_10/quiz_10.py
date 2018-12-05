# Lets the user input a number N between 1 and 10 and a number k
# at most equal to N!, and outputs the kth permutation of {0, ..., N-1},
# using lexicographic order and counting from 1.
#
# Written by *** and Eric Martin for COMP9021

import sys
from math import factorial


provided_input = input('Enter two strictly positive integers,\n'
                       '  the first one at most equal to 10\n'
                       '  the second one at most equal to first one!: ')
provided_input = provided_input.split()
if len(provided_input) != 2:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    number_range = int(provided_input[0])
    rank = int(provided_input[1])
    if number_range <= 0 or rank <= 0 or rank > factorial(number_range):
        raise ValueError
except:
    print('Incorrect input, giving up.')
    sys.exit()

solution = ''

def permutate(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in permutate(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] woraks in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

solution_list =list(permutate(list(range(number_range))))
solution_list.sort()
solution_str = [str(i) for i in solution_list[rank-1]]
solution = "".join(solution_str)

print('Lexicographically, the permutation of 0, ..., {} of rank {} is: {}'.
                          format(number_range - 1, rank, solution))