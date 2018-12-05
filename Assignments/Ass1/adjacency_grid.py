# Assignment 1 for COMP2091
# Task 3: Adjacency_grid
# Written by Kun Zhang
# Aug 14, 2015
# ---------------------------------------------------------------
from itertools import permutations

# ---------------------------------------------------------------
# Function definition
def check_adj(x, y):
    return x == (y+1) or x == (y-1)


def print_result(R):
    for T in R:

        print(" \t%d\t " % T[0])
        print("%d\t%d\t%d" % (T[1], T[2], T[3]))
        print("%d\t%d\t%d" % (T[4], T[5], T[6]))
        print(" \t%d\t " % T[7])
        if T != R[-1]:
            print("\n",end="")

# ---------------------------------------------------------------
# Version 1
# insert redundant values in 1-D array
def get_result_v1(all_perm):
    for T in all_perm:
        # modify list
        Lo = list(T)
        L = Lo[:]          # keeping the original list
        # insert two values for mapping
        L.insert(4, L[-2])
        L.insert(-2, L[1])

        flag = 0
        for i in range(len(L) - 1):
            if check_adj(L[i], L[i+1]):#if there is adjacency
                flag = 0
                break                  # break
            else:
                flag = 1
        if flag == 1:
            # map back
            tb = (Lo[0], Lo[2], Lo[1], Lo[5], Lo[3], Lo[6], Lo[4], Lo[7])
        # print(tb)
            all_result.append(tb)

    all_result.sort()       # put in lexicographic order

# ---------------------------------------------------------------
# Version 2
# Create a 2D array
def get_result_v2(all_perm):
    for T in all_perm:
        t_array = [[-1 for i in range(5)] for j in range(6)]   # create 6*5 array with -1 filling
                                                                  # blanks

        # map all_perms to 2D array
        t_array[1][2] = T[0]
        t_array[2][1:4] = T[1:4]
        t_array[3][1:4] = T[4:7]
        t_array[4][2] = T[7]
        #print(t_array)
        flag = 1
        for i in range(1,5):
            for j in range(1,4):
                # check numerical adjacency for adjacent 4 cells
                if check_adj(t_array[i][j], t_array[i-1][j]) or \
                        check_adj(t_array[i][j], t_array[i+1][j]) or \
                        check_adj(t_array[i][j], t_array[i][j-1]) or \
                        check_adj(t_array[i][j], t_array[i][j+1]):
                        flag = 0
                        break
            if flag == 0:
                break

        if flag == 1:
             all_result.append(T)


if __name__ == "__main__":
    all_perm = list(permutations(range(1,9), 8))
    all_result = []
    get_result_v2(all_perm)
    print_result(all_result)


#    print("\nTotal of %d Solutions" % (len(all_result)/8))