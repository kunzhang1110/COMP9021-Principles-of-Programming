import math
input_roman = 'IXI'
generic_roman_input = 'MDCLXVI'
input_arabic = int('900000000000')
generic_roman_input_reversed = generic_roman_input[::-1]

# generic_roman_rule = []
# if len(generic_roman_input_reversed) == 1:
#     generic_roman_rule.append(1, generic_roman_input_reversed[0])
# else:
#     generic_roman_number = 1
#     for i in range(len(generic_roman_input_reversed)):
#         if i != 0:
#             if i % 2 == 0:
#                 generic_roman_number *= 2
#             else:
#                 generic_roman_number *= 5
#         generic_roman_rule.append((generic_roman_number, generic_roman_input_reversed[i]))
#
# generic_roman_rule_reversed = generic_roman_rule[::-1]
# pow_ten = []   # a list of generic that represents 10^x
# for a, r in generic_roman_rule_reversed[1:]:
#     if math.log10(a).is_integer():
#         pow_ten.append((a, r))
#
# for aten, rten in pow_ten:
#     for a, r in generic_roman_rule_reversed:
#         if 1 < a/aten <= 10:
#             generic_roman_rule.append((a - aten, rten + r))
# generic_roman_rule.sort(reverse=True)
# print(generic_roman_rule)
# converted_roman = ""
# for i in range(len(generic_roman_rule)):
#     occurrence = input_arabic//generic_roman_rule[i][0]
#     input_arabic %= generic_roman_rule[i][0]
#
#     for j in range(occurrence):
#         converted_roman += generic_roman_rule[i][1]
#
# if not input_arabic:
#     print(converted_roman)

# roman to arabic conversion
generic_roman_number = 1
generic_roman_rule = {} # a dictionary of (ROMAN: Arabic)
for i in range(len(generic_roman_input_reversed)):
    if i != 0:
        if i % 2 == 0:
            generic_roman_number *= 2
        else:
            generic_roman_number *= 5
    generic_roman_rule.setdefault(generic_roman_input_reversed[i], (i, generic_roman_number))

print(generic_roman_rule)

converted_arabic = 0
i = 0
while i < len(input_roman) :
    if i != len(input_roman) - 1:
        current_rank = generic_roman_rule[input_roman[i]][0]
        next_rank = generic_roman_rule[input_roman[i+1]][0]
    else:
        current_rank = next_rank
    if current_rank >= next_rank:
        converted_arabic += generic_roman_rule[input_roman[i]][1]
    else:
        converted_arabic += generic_roman_rule[input_roman[i+1]][1] - generic_roman_rule[input_roman[i]][1]
        i += 1
    i += 1

print(converted_arabic)
