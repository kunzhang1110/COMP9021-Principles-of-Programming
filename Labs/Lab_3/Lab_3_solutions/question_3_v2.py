# Finds all triples of positive integers (i, j, k) such that
# i, j and k are two digit numbers,
# no digit occurs more than once in i, j and k,
# and the set of numbers that occur in i, j or k is equal to
# the set of digits that occur in the product of i, j and k.
# Uses the built-in set data structure.
#
# Written by Eric Martin for COMP9021

# If i, j and k are numbers in the range [20, 99], i < j < k,
# and every digit occurs in at most one of i, j and k
# then i >= 12, i <= 76, i <= 87, and k <= 98. 
MIN = 12
MAX1 = 76
MAX2 = 87
MAX3 = 98

for i in range(MIN, MAX1 + 1):
    # Tests whether the two digits that occur in i are distinct.
    i_digits = {i // 10, i % 10}
    if len(i_digits) != 2:
        continue
    for j in range(i + 1, MAX2 + 1):
        # Tests whether the two digits that occur in j are distinct
        # and do not occur in i.
        j_digits = i_digits | {j // 10, j % 10}
        if len(j_digits) != 4:
            continue           
        for k in range(j + 1, MAX3 + 1):
            # Tests whether all digits that occur in k are distinct
            # and do not occur in either i or j.
            k_digits = j_digits | {k // 10, k % 10}
            if len(k_digits) != 6:
                continue
            product = i * j * k
            # Tests whether the set of digits that occur in i, j or k
            # is equal to the set of digits that occur in i * j * k.
            # Justified as product has at most 6 digits.
            if k_digits == set(int(d) for d in str(product)):
                print('{} x {} x {} = {}'.format(i, j, k, product))
