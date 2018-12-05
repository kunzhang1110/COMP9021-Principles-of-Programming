import itertools
user_input = input("Enter: ").split()
available_digits = [int(x) for x in user_input[0]]
desired_sum = int(user_input[1])

solution_count = 0
for r in range(1, len(available_digits)+1):
    for comb in itertools.combinations(available_digits, r):
        if sum(comb) == desired_sum:
            solution_count += 1

print(solution_count)