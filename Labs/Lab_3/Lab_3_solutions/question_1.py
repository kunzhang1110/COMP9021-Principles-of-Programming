# Finds all sequences of consecutive prime 5-digit numbers,
# say (a, b, c, d, e, f), such that
# b = a + 2, c = b + 4, d = c + 6, e = d + 8, and f = e + 10.
#
# Written by Eric Martin for COMP9021


from math import sqrt


def is_prime(n):
    # Only used to test odd numbers
    for d in range(3, round(sqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


print('The solutions are:\n')
# The list of all i's such that a + i is one of a, b, c, d, e, f
good_leaps = list(sum(range(0, k, 2)) for k in range(2, 13, 2))
for a in range(1001, 100000, 2):
    good_sextuple = True
    for i in range(0, good_leaps[-1] + 1, 2):
        # Testing a, b, c, d, e, f
        if i in good_leaps:
            if not is_prime(a + i):
                good_sextuple = False
                break
        # Testing the odd numbers between a and b, b and c,
        # c and d, d and e, e and f
        else:
            if is_prime(a + i):
                good_sextuple = False
                break
    if good_sextuple:
        for i in good_leaps[: -1]:
            print(a + i, end = '  ')
        print(a + good_leaps[-1])
