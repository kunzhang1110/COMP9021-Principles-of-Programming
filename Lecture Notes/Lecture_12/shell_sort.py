# Written by Eric Martin for COMP9021


def shell_sort(L):
    for n in range(len(L) // 2, 0, -1):
        # We use Pratt's method which uses as gaps all numbers of the form 2^i * 3^j
        p = n
        while p % 2 == 0:
            p //= 2
        while p % 3 == 0:
            p //= 3
        if p != 1:
            continue
        for i in range(n, 2 * n):
            for j in range(i, len(L), n):
                k = j
                while k >= n and L[k - n] > L[k]:
                    L[k - n], L[k] = L[k], L[k - n]
                    k -= n
