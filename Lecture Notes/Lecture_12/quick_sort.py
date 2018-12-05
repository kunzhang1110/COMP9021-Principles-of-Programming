# Written by Eric Martin for COMP9021


def quick_sort(L):
    quicksort(L, 0, len(L) - 1)

def quicksort(L, start, last):
    if last - start < 1:
        return
    split_point = partition(L, start, last)
    quicksort(L, start, split_point - 1)
    quicksort(L, split_point + 1, last)

def partition(L, start, end):
    pivot_value = L[start]
    left_mark = start + 1
    right_mark = end
    while True:
        while left_mark <=  right_mark and L[left_mark] <= pivot_value:
            left_mark += 1
        while right_mark > left_mark and L[right_mark] >= pivot_value:
            right_mark -= 1
        if right_mark <= left_mark:
            break
        if left_mark != right_mark:
            L[left_mark], L[right_mark] = L[right_mark], L[left_mark]
            left_mark += 1
            rigth_mark -= 1
    if left_mark == right_mark:
        right_mark -= 1
    if right_mark > start:
        L[start], L[right_mark] = L[right_mark], L[start]
    return right_mark
                    

                    
