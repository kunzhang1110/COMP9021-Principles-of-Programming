# Randomly fills a grid of size 10 x 10 with 0s and 1s
# and computes the size of the largest area with a checkers pattern.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randint

dim = 10
grid = [[None] * dim for _ in range(dim)]

def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            if grid[i][j]:
                print(' 1', end = '')
            else:
                print(' 0', end = '')
        print()
    print()

def explore_from(i, j):
#    print(i, j)
    return  checker_area(i, j, -1)


def checker_area(i, j, caller_grid):
    try:
        this_grid = grid[i][j]
    except IndexError:
        return 0

    if i < 0 or j < 0:
        return 0
#    print(this_grid, caller_grid)

    if (i, j) in explored:
        return 0
    else:
        explored.append((i, j))
#        print(explored)

    if this_grid == caller_grid:
        return 0

    # if this grid is different from caller grid, explores the adjacent
    sum = checker_area(i,j+1,this_grid) + checker_area(i,j-1, this_grid) \
           + checker_area(i+1,j, this_grid) + checker_area(i-1, j, this_grid) + 1
#    print(sum)
    return sum


provided_input = input('Enter 2 integers, '
                        'the second one being nonnegative: ')
provided_input = provided_input.split()
#provided_input = (0, 3)
if len(provided_input) != 2:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    seed_arg, density, = (int(i) for i in provided_input)
    if density < 0:
        raise ValueError
except:
    print('Incorrect input, giving up.')
    sys.exit()

seed(seed_arg)
# We fill the grid with randomly generated 0s and 1s,
# with for every cell, a probability of 1/(density + 1) to generate a 0.
for i in range(dim):
    for j in range(dim):
        grid[i][j] = int(randint(0, density) != 0)
print('Here is the grid that has been generated:')
display_grid()

max_size_of_region_with_checkers_structure = 0

for i in range(dim):
    for j in range(dim):
        explored = []
        size_of_region_with_checkers_structure = explore_from(i, j)
#        print(size_of_region_with_checkers_structure)
        if  max_size_of_region_with_checkers_structure < size_of_region_with_checkers_structure:
            max_size_of_region_with_checkers_structure = size_of_region_with_checkers_structure


# i = 3
# j = 2
# max_size_of_region_with_checkers_structure = checker_area(i, j,-1)

print('The size of the largest area with a checkers structure '
      'is {}'.format(max_size_of_region_with_checkers_structure))
