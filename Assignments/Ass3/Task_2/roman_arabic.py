import sys
import re
import math
import itertools
import string

input_args = sys.argv[1:]


def print_wrong_arg():
    print("""I expect one, two or three command line arguments,
  the second one being "minimally" in case two of those are provided
  and "using" in case three of those are provided.""")
    sys.exit()


def print_wrong_sequence():
    print("""The provided sequence of so-called generalised roman symbols is invalid,
  either because it does not consist of letters only
  or because some letters are repeated.""")
    sys.exit()


def print_invalid_number():
    print("""The input is not a valid arabic number,
  or is too large an arabic number,
  or is not a valid (possibly generalised) roman number,
  depending on what is expected.""")
    sys.exit()


def check_input_arabic(arab,r):
    r_len = len(r)
    if r_len%2 != 0:  # if rule has odd char
        range_limit = 10 ** (r_len//2) * 4
    else:
        range_limit = 10 ** (r_len//2 - 1) * 9
    if arab not in range(1,range_limit):
        print_invalid_number()


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


def check_one_input(one_input, rule="MDCLXVI"):
    # one input should be either valid arabic < 4000 or valid roman
    try:
        if re.match(r'[0]+\d*', one_input): # check if there is any leading zero
            print_invalid_number()
        else:
            arabic = int(one_input)
            check_input_arabic(arabic, rule)
            return arabic
    except ValueError:
        roman = one_input
        if check_roman(roman, rule):
            return roman
        else:
             print_invalid_number()
    else:
        print_wrong_arg()


def check_two_inputs():
    # first one should be valid generalised roman; second one is "minimally"
    # this function does not check if a generalised roman can be generated or not
    # it only checks if the input generalised roman has correct syntax

    if input_args[1] != "minimally":
        print_wrong_arg()
    if re.search(r'[^a-zA-Z]+', input_args[0]):  # if not letters
        print_invalid_number()
    else:
        return input_args[0]


def check_rule(gen_rule):
    # a valid rule should consist of non-repeated char
    # all letters
    set_gen_rule = set(gen_rule)
    if len(set_gen_rule) != len(gen_rule):
        return False
    if re.search(r'[^a-zA-Z]+', gen_rule):  # if not letters
        return False
    return True


def check_three_inputs():
    # first one should be valid arabic or roman; second one is "using" and
    # third one is a valid rule
    if input_args[1] != "using":
        print_wrong_arg()
    rule = input_args[2]
    if not check_rule(rule):
        print_wrong_sequence()
    check_three_input_val = check_one_input(input_args[0], rule)
    return check_three_input_val, rule


def roman_to_arabic(input_roman, generic_rule_input="MDCLXVI"):
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
    #print(generic_roman_rule)
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


def arabic_to_roman(input_arabic, generic_rule_input="MDCLXVI"):
    # convert arabic to roman
    generic_rule_input_reversed = generic_rule_input[::-1]
    generic_roman_rule = []
    if len( generic_rule_input_reversed) == 1:  # obtain a list of (arabic value, rule) with order preserved
        generic_roman_rule.append(1,  generic_rule_input_reversed[0])
    else:
        generic_roman_number = 1 # the smallest representation of roman number is 1
        for i in range(len( generic_rule_input_reversed)):
            if i != 0: # if even than times by 2
                if i % 2 == 0: # if even
                    generic_roman_number *= 2
                else:  # if odd than times by 5
                    generic_roman_number *= 5
            generic_roman_rule.append((generic_roman_number,  generic_rule_input_reversed[i]))

    generic_roman_rule_reversed = generic_roman_rule[::-1]
    pow_ten = []   # a list of generic that represents 10^x
    for a, r in generic_roman_rule_reversed[1:]:
        if math.log10(a).is_integer():
            pow_ten.append((a, r))

    for aten, rten in pow_ten: # generate a list of pair-subtraction from the rule like [10, 9, 5, 4, 1]
        for a, r in generic_roman_rule_reversed:
            if 1 < a/aten <= 10:
                generic_roman_rule.append((a - aten, rten + r))
    generic_roman_rule.sort(reverse=True)
#    print(generic_roman_rule)
    converted_roman = ""
    for i in range(len(generic_roman_rule)):
        occurrence = input_arabic//generic_roman_rule[i][0] # check if input value is greater than rule value
        input_arabic %= generic_roman_rule[i][0] # get the remainder

        for j in range(occurrence): # if the input value is greater, than it can be represented by a roman letter
            converted_roman += generic_roman_rule[i][1]

    if not input_arabic: # if can be converted
        return converted_roman
    else:
        return False


def one_input_conversion(input_value):
    if type(input_value) == str: # if roman input
        converted_arabic = roman_to_arabic(input_value)
        print(converted_arabic)
    else: # if arabic input
        converted_roman = arabic_to_roman(input_value)
        print(converted_roman)
        sys.exit()


def three_input_conversion(input_value, rule):
    if type(input_value) == str: # if roman input
        converted_arabic = roman_to_arabic(input_value, rule)
        print(converted_arabic)
    else: # if arabic input
        converted_roman = arabic_to_roman(input_value, rule)
        print(converted_roman)
        sys.exit()


def two_input_conversion(input_roman):
    def check_possible_rule(possible_rule, extra_letters):
        possible_rule_reverse = possible_rule[::-1]
        rule_len = len(possible_rule)
        for i in range(rule_len):
            if possible_rule_reverse[i] in extra_letters and (i % 2 == 0 or i == rule_len - 1):   # extra letters cannot be in
                return False                                   # even space (can only be fives)
            if possible_rule_reverse[i] in repeated_roman and i % 2 == 1:   # repeated roman should be in odd space (10s)
                return False
        return True

    i = 0
    repeated_roman = []     # repeated roman characters are in power of 10 from big to small
 #   repeated_roman_adj = []   # adjacent repeat

    while i < len(input_roman):
        j = i + 1
        while j < len(input_roman):
            if input_roman[i] == input_roman[j] and input_roman[i] not in repeated_roman:
                repeated_roman.append(input_roman[i])
#                if j == i + 1:
#                   repeated_roman_adj.append((input_roman[i]))
                if j - i > 3:
                    print_invalid_number()
            j += 1
        i += 1
    # non_repeated_roman = []
    # for i in input_roman:
    #     if i not in repeated_roman and i not in non_repeated_roman:
    #         non_repeated_roman.append(i)

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
            break
        null_char += 1

    smallest_arabic_rule_string = ""
    for letter in smallest_arabic_rule:
        if letter not in used_letters:
            smallest_arabic_rule_string += "_"
        else:
            smallest_arabic_rule_string += letter
    if smallest_arabic == sys.maxsize:
        print_invalid_number()
    else:
        print(smallest_arabic,'using', smallest_arabic_rule_string)
    return


# Main Program =========================================================
if __name__ == "__main__":
    input_len = len(input_args)
    if input_len not in [1, 2, 3]:
        print_wrong_arg()
    elif input_len == 1:  # one input either arabic or roman
        input_value = check_one_input(input_args[0])
        one_input_conversion(input_value)
    elif input_len == 2:  # two inputs roman + minimally
        input_value = check_two_inputs()
        two_input_conversion(input_value)
    else:   # three inputs arabic + roman + minimally
        input_value, rule = check_three_inputs()
        three_input_conversion(input_value, rule)

