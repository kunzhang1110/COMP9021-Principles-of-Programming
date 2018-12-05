#  change non-greedy

user_input = input("Input pairs:")
all_notes = []
while user_input:
    face_value, note_number = user_input.split(":")
    for i in range(int(note_number)):
        all_notes.append(int(face_value))
    user_input = input()

desire_amount = int(input("Desired amount:"))

all_path = [[0]] * (desire_amount + 1)
all_number = [0] * (desire_amount + 1)
note_type = set(all_notes)

def check_note(x):
    all_notes_copy = all_notes.copy()
    for c in all_path[amount - x]:
        if c in all_notes_copy:
            all_notes_copy.remove(c)
    return x in all_notes_copy


for amount in range(desire_amount + 1):
    if amount in note_type:
        all_number[amount] = 1
        all_path[amount] = [amount]
        continue
    min_number_note = amount
    correct_note = 0
    for note in [x for x in note_type if x < amount and check_note(x)]:
        if all_number[amount-note] < min_number_note:
            min_number_note = all_number[amount-note]
            correct_note = note
    if min_number_note != amount:
        all_number[amount] = all_number[amount-correct_note] + 1
        all_path[amount] = all_path[amount-correct_note] + [correct_note]

print(all_path[-1])
dic = {}
for x in all_path[-1]:
    dic[x] = dic.setdefault(x, 0) + 1
dic_list = []
for key in dic:
    dic_list.append((key, dic[key]))
dic_list.sort()
for t in dic_list:
    print("${} : {}".format(t[0], t[1]))
