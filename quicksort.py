# Author:Chipo
# Date:11/3/2022
# Purpose:Lab 3


# Partition function
def partition(the_list, p, r, compare_func):
    i = p - 1
    j = p
    pivot = the_list[r]

    # condition
    while j < r:

        #  if j-index value is smaller
        if compare_func(the_list[j], pivot):
            temp = the_list[i + 1]
            the_list[i + 1] = the_list[j]
            the_list[j] = temp
            i = i + 1

        j = j + 1  # j increases in each iteration whether if statement met or not

    # at the end of the iteration
    temp = the_list[i + 1]
    the_list[i + 1] = pivot
    the_list[r] = temp

    return i + 1


# Quicksort function
def quicksort(the_list, p, r, compare_func):
    if p >= r:
        return

    x = partition(the_list, p, r, compare_func)

    quicksort(the_list, p, x - 1, compare_func)
    quicksort(the_list, x + 1, r, compare_func)


# sort function
def sort(the_list, compare_func):
    p = 0
    r = len(the_list) - 1

    quicksort(the_list, p, r, compare_func)
    return the_list
