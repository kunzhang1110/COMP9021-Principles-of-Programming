def find_all_divisor(n):
    return [i for i in range(1, n) if n % i == 0]

for n in range (100, 1000):
    if sum(find_all_divisor(n)) == n:
        print(n)
