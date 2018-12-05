# optimal the minimal number of banknotes
import re
import itertools

# print("Input pairs:")
# user_input = input()
# all_user_input = [user_input]
# while 1:
#     user_input = input()
#     if user_input:
#         all_user_input.append(user_input)
#     else:
#         break

all_user_input = ['1:100', '2:5', '3:4', '10:5', '20:4', '30:1']
#all_user_input = ['1:30', '20:30', '50:30']
desire_amount = 107

all_notes = []
for pair in all_user_input:
    pair_match = re.match('(\d+):(\d+)', pair)
    for num in range(int(pair_match.group(2))):
        all_notes.append(int(pair_match.group(1)))

r = 2
flag = 0
while r< len(all_notes):
    for comb in set(itertools.combinations(all_notes, r)):
        if sum(comb) == desire_amount:
            print(comb)
            flag = 1
            break
    if flag == 1:
        break
    r += 1
    print(r)