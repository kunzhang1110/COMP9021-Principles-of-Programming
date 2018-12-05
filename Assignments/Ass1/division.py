# Assignment 1 for COMP2091
# Task 4: A Division
# Written by Kun Zhang
# Aug 14, 2015
# ---------------------------------------------------------------
import itertools

# ---------------------------------------------------------------
def check_step_1(a, divisor):       # 1st bit of quotient
    step_1_digits = []
    for i in range(1,10):
        prd = i * divisor
        if str(prd)[2:] == a + a and prd > 999:     # **aa
            step_1_digits.append(i)
    return step_1_digits

def check_step_2(a, divisor):          # 2nd bit of quotient
    step_2_digits = []
    for i in range(10):
        prd = i * divisor
        if str(prd)[-1] == a and prd > 999 :        # ***a
            step_2_digits.append(i)
    return step_2_digits

def check_step_3(a, divisor):   # third bit of quotient
    prd = int(a) * divisor
    if str(prd)[1] == a:                # *a**
        return [int(a)]

def check_step_4(a, divisor):  # last bit of quotient
    step_4_digits = []
    for i in range(10):
        prd = i * divisor
   #     if a not in prd and prd > 999:
        if prd > 999:                     # ****
            step_4_digits.append(i)
    return step_4_digits

# get quotient
def get_quo(a, b, c, d):
    l = [a, b, c, d]
    quo = []
    temp = list(itertools.product(*l)) # cartesian product of a, b, c, d
    for q in temp:
        a = [str(x) for x in q]        # concatenate digits
        quo.append(int("".join(a)))     # convert to int
    return quo

# ---------------------------------------------------------------
def find_divisor_quotient():
    for divisor in range(100, 1000):
        a = str(divisor)[1]
        if a == '0':        # a cannot be zero
            continue

        # check all partial products, return valid bit of quotient
        step_1_bit = check_step_1(a, divisor)
        step_2_bit = check_step_2(a, divisor)
        step_3_bit = check_step_3(a, divisor)
        step_4_bit = check_step_4(a, divisor)

        # if all digits are valid
        if step_1_bit and step_2_bit and step_3_bit and step_4_bit:
            quo_ls = get_quo(step_1_bit, step_2_bit, step_3_bit, step_4_bit)
            for q in quo_ls:
                product = divisor * q
                if str(product)[4] == a:    # if the product is valid
                    div = divisor
                    quo = q
                    prd = product
                    return div, quo, prd

# ---------------------------------------------------------------
# check the validity of solution
def check_solution(div, quo):
    quo = str(quo)
    for q in quo:
        print(div*int(q))

# ---------------------------------------------------------------
if __name__ == "__main__":
    div, quo, prd= find_divisor_quotient()
    print("{} / {} = {} is the solution.".format(prd,div,quo))
#    check_solution(div, quo)