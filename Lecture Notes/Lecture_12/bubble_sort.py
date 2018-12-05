# Written by Eric Martin for COMP9021


def bubble_sort(L):
    bound = len(L) - 1
    swapped = True
    while swapped and bound:
        swapped = False
        for i in range(bound):
            if L[i] > L[i + 1]:
                L[i], L[i + 1] = L[i + 1], L[i]
                swapped = True
                bound = i
