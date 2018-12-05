# Assignment 1 for COMP2091
# Task 1: An Equation
# Written by Kun Zhang
# Aug 13, 2015

# create a list for all possible abcdefg;
# all_digits[0] = a,
# all_digits[6] = g

# version 1 takes 47s
# version 2 takes 11s
# ---------------------------------------------------------------
# import time

# ---------------------------------------------------------------
# Version 1
def check_equation_v1(n):
    n_ls = [int(x) for x in str(n)]
    a = n_ls[0]
    b = n_ls[1]
    c = n_ls[2]
    d = n_ls[3]
    e = n_ls[4]
    f = n_ls[5]
    g = n_ls[6]

    if (a and b and c and d and e and f and g) == 0:
        return False

    LHS = (100 * a + 10 * b + c) * (10 * d + e) * (10 * f + g)
    RHS = a * (10 * b + c) * (1000 * d + 100 * e + 10 * f + g)
    # print out results
    if LHS == RHS:
        result.append((a, b, c, d, e, f, g))
    else:
        return False

# ---------------------------------------------------------------
# Version 2
def check_equation_v2(n):
    a = n//(10**6)
    b = (n%10**6)//10**5
    c = (n%10**5)//10**4
    d = (n%10**4)//10**3
    e = (n%10**3)//10**2
    f = (n%10**2)//10**1
    g =  n % 10**1

    if (a and b and c and d and e and f and g) == 0:
        return False

    LHS = (100 * a + 10 * b + c) * (10 * d + e) * (10 * f + g)
    RHS = a * (10 * b + c) * (1000 * d + 100 * e + 10 * f + g)
    # print out results
    if LHS == RHS:
        result.append((a, b, c, d, e, f, g))
    else:
        return False

def print_result(result):
    print("There are %d solutions:" % len(result))
    for a, b, c, d, e, f, g in result:
        print("{}{}{} * {}{} * {}{} = {} * {}{} * {}{}{}{}".format(a,b,c,d,e,f,g,a,b,c,d,e,f,g))

# ---------------------------------------------------------------
# main program
if __name__ == "__main__":
#    start_time = time.time()

    result = []
    for i in range(1111111, 10000000):
        check_equation_v2(i)
    print_result(result)

#    print(time.time()-start_time," seconds")