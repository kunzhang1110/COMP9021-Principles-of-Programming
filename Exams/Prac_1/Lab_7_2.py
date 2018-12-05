# change problem non-greedy
# dynamic programming

desired_amount = int(input("Input desired amount:"))
all_notes = []
print("Available_notes")
while True:
    user_input = input()
    if not user_input:
        break
    note, num_of_note = (int(x) for x in user_input.split(sep=":"))
    for i in range(num_of_note):
        all_notes.append(note)

note_type = set(all_notes)
print(note_type)

all_path_length = [0] * (desired_amount + 1)
all_path = [[0]] * (desired_amount + 1)



def check_rest_notes(amount, note):
    rest_notes = all_notes.copy()
    for i in all_path[amount - note]:
        if i in rest_notes:
            rest_notes.remove(i)
    if note in rest_notes:
        return True
    return False

for amount in range(0, desired_amount + 1):
    if amount in note_type:
        all_path_length[amount] = 1
        all_path[amount] = [amount]
        continue
    min_path_len = amount
    min_note = 0
    for note in [x for x in note_type if amount > x and check_rest_notes(amount, x)]:
        if all_path_length[amount - note] < min_path_len and all_path_length[amount - note]:
            min_path_len = all_path_length[amount - note]
            min_note = note
    if min_path_len != amount:
        all_path_length[amount] = all_path_length[amount - min_note] + 1
        all_path[amount] = all_path[amount - min_note] + [min_note]

dic = {}
for i in all_path[-1]:
    dic[i] = dic.setdefault(i, 0) + 1
all_answer = []
for key in dic:
    all_answer.append((key, dic[key]))
all_answer.sort()
for t in all_answer:
    print("${}: {}".format(t[0], t[1]))
