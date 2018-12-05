# Written by Eric Martin for COMP9021


def selection_sort(L):
    bound = len(L) - 1
    for i in range(len(L) - 1):
        index_of_min = i
        for j in range(i + 1, len(L)):
            if L[j] < L[index_of_min]:
                index_of_min = j
        if index_of_min != i:
            L[i], L[index_of_min] = L[index_of_min], L[i]
