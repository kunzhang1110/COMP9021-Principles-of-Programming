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

a = [0, 1, 2]
b = [0, 2]
print(check_sublist(b, a))