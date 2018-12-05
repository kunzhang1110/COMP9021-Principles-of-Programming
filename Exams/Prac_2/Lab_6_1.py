import itertools
available_digits = "1234321"
desired_sum = 5

available_digits_list = [int(x) for x in available_digits]

number_of_sol = 0
for r in range(len(available_digits)):
    for comb in itertools.combinations(available_digits_list,r):
        if sum(comb) == desired_sum:
            number_of_sol += 1
print(number_of_sol)