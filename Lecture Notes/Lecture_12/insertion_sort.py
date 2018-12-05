# Written by Eric Martin for COMP9021


def insertion_sort(L):
    for i in range(1, len(L)):
        j = i
        while j and L[j - 1] > L[j]:
            L[j - 1], L[j] = L[j], L[j - 1]
            j -= 1
