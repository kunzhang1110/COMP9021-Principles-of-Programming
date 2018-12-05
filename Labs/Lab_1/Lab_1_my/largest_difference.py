from random import randint

L1 = [randint(-50, 50) for x in range(10)]
L2 = [randint(-50, 50) for x in range(10)]
d = [abs(L1[x] - L2[x]) for x in range(10)]
print(max(d))