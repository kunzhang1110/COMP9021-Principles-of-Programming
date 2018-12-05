# Assignment 1 for COMP2091
# Task 2: Multiple_2004
# Written by Kun Zhang
# Aug 13, 2015
# ---------------------------------------------------------------
import sys, re

# ---------------------------------------------------------------
# Version 1
# List all possible A2004B and store the smallest
def find_min_multiple_v1():
    min_M = 10**10
    min_A = 0
    min_B = 0
    min_N = 0
    for i in range(1,5):        # i is the length of A and B
        for A in range (10**(i-1), 10**i):      # generate all A from 10^(i-1)
                                                #as A = 00X is X
            for B in range(1, 10**i):       # generate all B from 1
                str_N = str(A) + "2004" + str(B)    # concatenate strings into A2004B
                N = int(str_N)
              #  print(N)
                if N % 2004 == 0:
                    M = N/2004
                    if min_M > M:   #check if M is smaller
                        min_M = M   #update M, A, B, N
                        min_A = A
                        min_B = B
                        min_N = N
                    #print("A =", A, ", B =", B, ", N =", N, ", M=", M)

    print("A =", min_A, ", B =", min_B, ", N =", min_N, ", M=", min_M)

# ---------------------------------------------------------------
# Version 2
# Generate a sorted list for A2004B with a length size_A_B
def find_min_multiple_v2():
    size_A_B = 2;
    while True:
        for size_A in range (1,size_A_B):
            all_number = [] # all number for size_A_B in the form of A2004B
            size_B = size_A_B - size_A
            for A in range(10**(size_A-1), 10**size_A): # generate A
                for B in range(10**(size_B-1), 10**size_B): # generate B
                    str_N = str(A) + "2004" + str(B)
                    N = int(str_N)
                    all_number.append(N)    #get all possible number of size_A_B+4 digits
        all_number.sort()
        # find the smallest multiple in the current list
        for N in all_number:
            if N%2004 == 0:
                    M = N/2004
                    N_str = str(N)
                    AB = re.search(r'(\d+)2004(\d+)', N_str) # Extract A and B
                    print("A =", AB.group(1), ", B =", AB.group(2), ", N =", N, ", M=", M)
                    return
        size_A_B += 1

# ---------------------------------------------------------------
# Version 3
def find_min_multiple_v3():
    M = 120140//2004                # the smallest number is 120140
    N = M * 2004                    # the smallest possible multiple of 2004
    while True:
        N_str = str(N)
        AB = re.search(r'(\d+)2004(\d+)', N_str) # Extract A and B
        if AB:
            print("A =", AB.group(1), ", B =", AB.group(2), ", N =", N)
            return
        N += 2004
        M += 1

if __name__ == "__main__":
    #find_min_multiple_v1()
    #find_min_multiple_v2()
    find_min_multiple_v3()