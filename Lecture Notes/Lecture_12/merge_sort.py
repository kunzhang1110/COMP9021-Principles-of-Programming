# Written by Eric Martin for COMP9021


def merge_sort(L):
    L_copy = list(L)
    mergesort(L, L_copy, 0, len(L))

def mergesort(L1, L2, start, end):
    if end - start < 2:
        return
    half_length = start + (end - start) // 2
    mergesort(L2, L1, start, half_length)
    mergesort(L2, L1, half_length, end)
    i = start
    i1 = start
    i2 = half_length
    while i1 < half_length and i2 < end:
        if L2[i1] <= L2[i2]:
            L1[i] = L2[i1]
            i1 += 1
        else:
            L1[i] = L2[i2]
            i2 += 1
        i += 1
    while i1 < half_length:
        L1[i] = L2[i1]
        i1 += 1
        i += 1
    while i2 < end:
        L1[i] = L2[i2]
        i2 += 1
        i += 1

                    
