import itertools

for perm in itertools.permutations(range(1,10)):
    if sum(perm[0:3]) == sum(perm[6:]) == 15 \
        and sum(perm[0::3]) == sum(perm[2::3]) == 15\
        and perm[4] == 5:
        print(perm)
