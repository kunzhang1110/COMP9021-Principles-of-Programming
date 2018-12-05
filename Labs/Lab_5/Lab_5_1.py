import itertools
p = itertools.permutations(range(1,10))

def test_sum(ls):
    if sum(i[0:3]) == 15 and  sum(i[3:6]) == 15 and \
       sum(i[0:7:3])== 15 and sum (i[1:8:3])==15 and\
       sum(i[0:10:4])==15:
        return True
    
for i in list(p):
    if test_sum(i):
        print(i)


