# From L and S input by the user as two relatively prime numbers,
# generates a linked list of length L, and reorders the list by
# starting with the Sth element (numbering elements of the list from 1),
# at each step jumping over S-1 elements, and looping around when needed.
# Eventually the original will have a new head and consist
# of the same nodes, but linked differently.

import sys
from random import seed, randrange
from linked_list import *
from extended_linked_list import ExtendedLinkedList

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def collect_references(L, length):
    node = L.head
    references = set()
    for i in range(length):
        references.add(id(node))
        node = node.next_node
    return references


# provided_input = input('Enter 3 integers: ')
# try:
#      provided_input = [int(arg) for arg in provided_input.split()]
# except ValueError:
#     print('Incorrect input (not all integers), giving up.')
#     sys.exit()
#
# if len(provided_input) != 3:
#     print('Incorrect input (not 3 arguments), giving up.')
#     sys.exit()
# for_seed, length, step = provided_input
# if length <= 0 or step <= 0:
#     print('Incorrect input (2nd or 3rd integers not strictly positive, '
#           'giving up.')
#     sys.exit()
# if gcd(length, step) != 1:
#     print('List length and step should be relatively prime, giving up.')
#     sys.exit()
for_seed, length, step = (2015, 8, 1)
seed(for_seed)

L = [0] * length
for i in range(length):
    L[i] = randrange(100)

LL = ExtendedLinkedList(L)
LL.print()
references = collect_references(LL, length)
LL.rearrange(step)
if collect_references(LL, length) != references:
    print('You cheated!')
    sys.exit()
else:
    LL.print()

