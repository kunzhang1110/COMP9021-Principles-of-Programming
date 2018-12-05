import itertools
available_digit_input = '1234321'
desired_sum_input = '5'
number_of_solution = 0

available_digit = [int(s) for s in available_digit_input]
desired_sum = int(desired_sum_input)

for number_of_digit in range(2,len(available_digit)+1):
    for comb in itertools.combinations(available_digit,number_of_digit):
        comb_sum = sum(comb)
        if comb_sum == desired_sum:
            number_of_solution += 1
print("There are ", number_of_solution, "solutions")