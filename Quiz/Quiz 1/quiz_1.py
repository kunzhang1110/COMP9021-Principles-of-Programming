# Generates a list of 10 random numbers between 0 and 19 included,
# and determines the length of the longest strictly increasing sequence and
# the smallest most frequent element in the list.
#
# Writtten by Kun Zhang and Eric Martin for COMP9021
# Quiz 1

import sys
from random import seed, randint


nb_of_elements = 10

try:
     seed(input('Enter an integer: '))
except TypeError:
    print('Incorrect input, giving up.')
    sys.exit()

L = []
for _ in range(nb_of_elements):
    L.append(randint(0, 20))
print('The generated list is:', L)

length_of_longest_increasing_sequence = 1
current_length = 1

smallest_most_frequent = None
largest_count = 0

# longest strictly increasing sequence
pre = 0
increasing_seq = 1
for i in L:
    if pre < i:
        increasing_seq += 1
    else:
        increasing_seq = 1
    if increasing_seq > length_of_longest_increasing_sequence:
        length_of_longest_increasing_sequence = increasing_seq
    pre = i

# smallest most frequent element
# make histogram
hist = {}
for i in L:
    hist[i] = hist.setdefault(i,0) + 1
max_hist = max(hist.values())    # find the most frequent values
most_freq = []                     #put in a list
for key in hist:
    if hist[key] == max_hist:
        most_freq.append(key)
smallest_most_frequent = min(most_freq)         # find the smallest

print('The length of the longest strictly increasing sequence is: {}'.format(
                                        length_of_longest_increasing_sequence))
print('The smallest most frequent element in the sequence is: {}'.format(
                                                       smallest_most_frequent))

