# Finds all triples of positive integers (i, j, k) such that
# i, j and k are two digit numbers,
# no digit occurs more than once in i, j and k,
# and the set of numbers that occur in i, j or k is equal to
# the set of digits that occur in the product of i, j and k.
#
# Written by Eric Martin for COMP9021

# If i, j and k are numbers in the range [20, 99], i < j < k,
# and every digit occurs in at most one of i, j and k
# then i >= 12, i <= 76, i <= 87, and k <= 98. 
MIN = 12
MAX1 = 76
MAX2 = 87
MAX3 = 98

# Extracts both digits d1 and d2 that occur in i, and examines whether
# the d1-st or d2-nd bit of digits is set to 1.
# If that is the case, returns False to indicate that a second occurrence
# of d1 or d2 has been found in candidate solution member.
# Otherwise, sets d1-st and d2-nd bits of digits to 1 and returns digits.
def test1(i, digits):
    digits = test1_aux(i, digits)
    if digits:
        return test1_aux(i // 10, digits)
    return False

def test1_aux(i, digits):
    dig = 1 << i % 10;
    if digits & dig:
        return False
    return digits | dig

# Extracts each digit dig that occurs in i, from right to left,
# and examines whether the dig-th bit of digits is set to 1.
# If that is the case, returns False to indicate that
# a second occurrence of dig  has been found in candidate solution member.
# Otherwise, sets dig-th bit of digits to 1.
# Finally, returns True if the resulting number is equal to digits,
# and 0 otherwise.
def test2(i, digits):
    other_digits = 0
    while i:
        other_digits |= 1 << i % 10
        i //= 10
    if digits == other_digits:
        return True
    return False

print('The solutions are:')
for i in range(MIN, MAX1 + 1):
    # Tests whether the two digits that occur in i are distinct.
    i_digits = test1(i, 0)
    if not i_digits:
        continue
    for j in range(i + 1, MAX2 + 1):
        # Tests whether the two digits that occur in j are distinct
        # and do not occur in i.
        j_digits = test1(j, i_digits)
        if not j_digits:
            continue           
        for k in range(j + 1, MAX3 + 1):
            # Tests whether all digits that occur in k are distinct
            # and do not occur in either i or j.
            k_digits = test1(k, j_digits)
            if not k_digits:
                continue
            product = i * j * k
            # Tests whether the set of digits that occur in i, j or k
            # is equal to the set of digits that occur in i * j * k.
            if test2(product, k_digits):
                print('{} x {} x {} = {}'.format(i, j, k, product))
