import numpy as np


def selection_sort_ascending(arr):
    i = 0
    while i < len(arr):
        j = i + 1
        min_i = i
        while j < len(arr):
            if arr[j] < arr[min_i]:
                min_i = j
            j += 1
        arr[i], arr[min_i] = arr[min_i], arr[i]
        i += 1
    print(arr)


def distribute(n, m, a):
    output_arr = np.zeros(m)
    selection_sort_ascending(a)
    for i in range(len(output_arr)):
        output_arr[i] = a[i]
    return output_arr


print(distribute(8, 5, np.array([3, 4, 1, 9, 56, 7, 9, 12])))