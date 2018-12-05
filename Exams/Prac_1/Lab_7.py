# Change making greedy

desired_amount = int(input("Input desired amount:"))
available_amount = [1, 2, 5, 10, 20, 50 ,100]
note_count = [0] * len(available_amount)
available_amount_reverse = available_amount.copy()
available_amount_reverse.reverse()

for i in range(len(available_amount_reverse)):
    while desired_amount - available_amount_reverse[i]>= 0:
        desired_amount -= available_amount_reverse[i]
        note_count[-(i+1)] += 1

if not desired_amount:
    print(available_amount, '\n', note_count)