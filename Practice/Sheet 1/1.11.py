"""
We have to increase or decrease every value of an array so that there is no negative integer values in the array
and the difference between the lowest value and highest value is minimized
"""
import numpy as np


def modify_arr_by_k(arr, k):
    selection_sort_ascending(arr)
    print(arr)
    arr[0] += k
    arr[len(arr) - 1] -= k
    diff = arr[len(arr) - 1] - arr[0]
    for i in range(1, len(arr) - 1):
        if arr[i] - k >= 0 and i > 1:
            arr[i] -= k
        else:
            arr[i] += k
    print(arr)
    return diff


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


arr1 = np.array([3, 9, 12, 16, 20])
print(modify_arr_by_k(arr1, 3))