# Randomly fills a grid of size 10 x 10 with digits between 0
# and bound - 1, with bound provided by the user.
# Given a point P of coordinates (x, y) and an integer "target"
# also all provided by the user, finds a path starting from P,
# moving either horizontally or vertically, in either direction,
# so that the numbers in the visited cells add up to "target".
# The grid is explored in a depth-first manner, first trying to move north, always trying to keep the current direction,
# and if that does not work turning in a clockwise manner.
#
# Written by Kun Zhang and Eric Martin for COMP9021


import sys
from random import seed, randrange
from array_stack import *


dim = 10
grid = [[0] * dim for _ in range(dim)]

def display_grid():
    for i in range(dim):
        print('    ', end = '')
        for j in range(dim):
            print(' ', grid[i][j], end = '')
        print()
    print()

def explore_depth_first(x, y, target):
    def explore(target, path, direction, current_sum, all_directions_copy):
        current_pos = path.peek()
        next_pos = (current_pos[0] + direction[0],
                                current_pos[1] + direction[1])
        if next_pos in path._data:
            return False
        if next_pos[0] not in range(dim) or next_pos[1] not in range(dim):
            return False
        new_sum = current_sum + grid[next_pos[0]][next_pos[1]]
        if new_sum > target:
            return False
        if new_sum == target:
            path.push(next_pos)
            return True
        if new_sum < target:
            path.push(next_pos)
            all_directions_copy.remove(direction)
            all_directions.insert(0, direction)

        for direction in all_directions_copy:
            if explore(target, path, direction, new_sum, all_directions_copy):
                return path
            else:
                continue
        return False

    all_directions = [(-1, 0), (0, 1), (1, 0),  (0, -1)]     # clockwise N, E, S, W
    path = ArrayStack()
    path.push((x, y))
    direction = all_directions[0]
    current_sum = grid[x][y]
    for direction in all_directions:
        if explore(target, path, direction, current_sum, all_directions):
            if len(path._data)<2:
                return None
            else:
                return path._data
            break
    return None

provided_input = input('Enter five integers: ').split()
if len(provided_input) != 5:
    print('Incorrect input, giving up.')
    sys.exit()    
try:
    seed_arg, bound, x, y, target = [int(x) for x in provided_input]
    if bound < 1 or x < 0 or x > 9 or y < 0 or y > 9 or target < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
    
seed(seed_arg)
# We fill the grid with randomly generated digits between 0 and bound - 1.
for i in range(dim):
    for j in range(dim):
        grid[i][j] = randrange(bound)
#print('Here is the grid that has been generated:')
#display_grid()

path = explore_depth_first(x, y, target)
if not path:
    print('There is no way to get a sum of {} starting '
          'from ({}, {})'.format(target, x, y))
else:
    print('With North as initial direction, and exploring '
          'the space clockwise,\n'
          'the path yielding a sum of {} starting from '
          '({}, {}) is:\n {}'.format(target, x, y, path))
           
