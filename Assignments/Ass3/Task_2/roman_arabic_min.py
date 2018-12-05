import itertools
import re
import string
import sys
import time
input_roman = 'ABCDEFA'
start_time = time.time()


def check_rule(gen_rule):
    # a valid rule should consist of non-repeated char
    # all letters
    set_gen_rule = set(gen_rule)
    if len(set_gen_rule) != len(gen_rule):
        return False
    if re.search(r'[^a-zA-Z]+', gen_rule):  # if not letters
        return False
    return True


def roman_to_arabic(input_roman, generic_rule_input="MDCLXVI"):
    roman_to_arabic_start = time.time()
    # roman to arabic conversion
    generic_rule_input_reversed = generic_rule_input[::-1]
    generic_roman_number = 1
    generic_roman_rule = {} # a dictionary of (ROMAN: (rank,Arabic value))
    for i in range(len(generic_rule_input_reversed)):  # generate the rule dictionary from input
        if i != 0:
            if i % 2 == 0:
                generic_roman_number *= 2
            else:
                generic_roman_number *= 5
        generic_roman_rule.setdefault(generic_rule_input_reversed[i], (i,generic_roman_number))
    # print(generic_roman_rule)
    converted_arabic = 0
    i = 0
    while i < len(input_roman) : # convert from roman to arabic according to the rule
        if i != len(input_roman) - 1:  # check if the number has higher rank than the next number
            current_rank = generic_roman_rule[input_roman[i]][0]
            next_rank = generic_roman_rule[input_roman[i+1]][0]
        else:
            current_rank = next_rank
        if current_rank >= next_rank:   # if next rank is lower, then not leading subtraction
            converted_arabic += generic_roman_rule[input_roman[i]][1]
        else:  # else is a leading subraction
            converted_arabic += generic_roman_rule[input_roman[i+1]][1] - generic_roman_rule[input_roman[i]][1]
            i += 1
        i += 1
    return converted_arabic

def check_roman(roman, r):
    # construct regular expression to match generic Roman rule
    if len(r)%2 != 0:   # if rule has odd number of element
        re_string = '^' + r[0] + "{0,3}"
        for i in range(1, len(r)):
            if i%2 ==0:
                re_string += "("
                for j in [2, 1]:
                    re_string += r[i] + r[i-j] + '|'
                re_string += r[i-1] + '?' + r[i] + "{0,3}"
                re_string += ")"
    else: # if rule has even number of element
        re_string =  ''
        for i in range(1, len(r)):
            if i == 1:
                j_range = [1]
            else:
                j_range = [2, 1]
            if i%2 !=0:
                re_string += "("
                for j in j_range:
                    re_string += r[i] + r[i-j] + '|'
                re_string += r[i-1] + '?' + r[i] + "{0,3}"
                re_string += ")"
    re_string += '$'
    roman_match = re.match(re_string,roman)
    if roman_match:
        return True
    else:
        return False

i = 0
repeated_roman = []     # repeated roman characters are in power of 10 from big to small
repeated_roman_adj = []   # adjacent repeat


while i < len(input_roman):
    j = i + 1
    while j < len(input_roman):
        if input_roman[i] == input_roman[j] and input_roman[i] not in repeated_roman:
            repeated_roman.append(input_roman[i])
            if j == i + 1:
                repeated_roman_adj.append((input_roman[i]))
            if j - i > 2:
                print("Error")
        j += 1
    i += 1
non_repeated_roman = []
for i in input_roman:
    if i not in repeated_roman and i not in non_repeated_roman:
        non_repeated_roman.append(i)

print(repeated_roman)
print(repeated_roman_adj)
print(non_repeated_roman)


def check_possible_rule(possible_rule, extra_letters):
    for i in range(len(possible_rule)):
        if possible_rule[i] in extra_letters and (i%2 != 0 or i == 0):   # extra letters cannot be in
            return False                                   # even space (can only be fives)
        if possible_rule[i] in repeated_roman and i%2 ==0:   # repeated roman should be in odd space (10s)
            return False
    return True


used_letters = list(set(input_roman))
not_used_letters = list(set(string.ascii_letters) - set(input_roman))  # letters not used in roman input

null_char = -1
smallest_arabic = sys.maxsize
smallest_arabic_rule = []
extra_letters = []
converted_arabic = sys.maxsize
while null_char < len(used_letters):
    if null_char> -1:
        extra_letters.append(not_used_letters[null_char])
    all_possible_rules = list(itertools.permutations(used_letters + extra_letters))
    for possible_rule in all_possible_rules:
        if not check_possible_rule(possible_rule, extra_letters):
            continue
        if check_roman(input_roman,possible_rule):
            converted_arabic = roman_to_arabic(input_roman, possible_rule)
        else:
            continue
        if converted_arabic < smallest_arabic:
            smallest_arabic = converted_arabic
            smallest_arabic_rule = possible_rule
    if smallest_arabic != sys.maxsize:
        print(smallest_arabic, smallest_arabic_rule)
        break
    print(smallest_arabic, possible_rule, time.time() - start_time, null_char)
    null_char += 1

smallest_arabic_rule_string = ""
for letter in smallest_arabic_rule:
    if letter not in used_letters:
        smallest_arabic_rule_string += "_"
    else:
        smallest_arabic_rule_string += letter

print(smallest_arabic,'using', smallest_arabic_rule_string)
print('{} s'.format((time.time()-start_time)))