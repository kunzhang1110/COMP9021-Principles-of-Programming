two_dic = {}
for x in range(0, 100):
    for y in range(0, 100):
        two_sq = x*x + y*y
        if two_sq in range (100, 1000):
            two_dic[two_sq] = two_dic.setdefault(two_sq,[]) + [(x, y)]

two_dic_n = list(two_dic.keys())
two_dic_n.sort()
print(two_dic_n)

for k in two_dic_n:
    if k + 1 in two_dic_n and k + 2 in two_dic_n:
        print("({:}, {:}, {:}) (equal to ({:}^2 + {:}^2 , {:}^2 + {:}^2,{:}^2 + {:}^2)) is a solution".
              format(k, k+1, k+2, two_dic[k][0][0], two_dic[k][0][1], two_dic[k+1][0][0], two_dic[k+1][0][1], two_dic[k+2][0][0], two_dic[k+2][0][1]))

