# Magic squares

import itertools


def check(p):
    # check row1 == row3 == col1 == col3 == 15 meaning row2 == col2 == 15
    # p[4] == 5 means diagonals are equal
    if (p[0] + p[1] + p[2] == 15) and (p[6] + p[7] + p[8] ==15) and \
            (p[0] + p[3] + p[6] == 15) and (p[2] + p[5] + p[8] == 15) and\
            p[4] == 5:
        return True
    return False

count = 0
for perm in itertools.permutations(range(1,10)):
    if check(perm):
        for i in range(len(perm)):
            print(perm[i], end=" ")
            if (i + 1)%3 == 0:
                print("")
        print("")
        count += 1

print("Total: ", count)

# Answer: Total = 8
