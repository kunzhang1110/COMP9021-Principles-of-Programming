import re

all_user_input = ['1:100', '2:5', '3:4', '10:5', '20:4', '30:1']
#all_user_input = ['2:10', '20:30', '50:10']
desire_amount =107

all_notes = []
for pair in all_user_input:
    pair_match = re.match('(\d+):(\d+)', pair)
    for num in range(int(pair_match.group(2))):
        all_notes.append(int(pair_match.group(1)))


def check_sublist(ls1, ls2):
    # sublist ls1 and list ls2
    list_1 = ls1.copy()
    list_2 = ls2.copy()
    for item in list_1:
        found = 0
        for i in range(len(list_2)):
            if item == list_2[i]:
                list_2.pop(i)
                found = 1
                break
        if not found:
            return False
    return True


def dpMakeChange(all_notes,change,minCoins,coinsUsed):
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coin_face if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount and (check_sublist(coinsUsed[cents-j+1] + [j] ,all_notes)):
                coinCount = minCoins[cents-j]+1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents+1] = coinsUsed[cents-newCoin+1] + [newCoin]
    return coinsUsed[cents]


coin_face = set(all_notes)
all_notes.append(0)
minCoins = [0]* (desire_amount+1)
coinsUsed = [[0]]* (desire_amount+2)
answer_list = dpMakeChange(all_notes,desire_amount,minCoins,coinsUsed)
dic={}
for i in [x for x in answer_list if x]:
    dic[i] = dic.setdefault(i,0) + 1
print_list = []
for key in dic:
    print_list.append((key, dic[key]))
print_list.sort()
for key, value in print_list:
    print("$",key, ": ", value)