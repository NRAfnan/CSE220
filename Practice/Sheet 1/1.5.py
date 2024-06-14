import numpy as np


def selection_sort(arr):
    current_i = 0
    while current_i < len(arr):
        min_index = current_i
        j = current_i + 1
        while j < len(arr):
            if arr[j] < arr[min_index]:
                min_index = j
            j += 1
        arr[current_i], arr[min_index] = arr[min_index], arr[current_i]
        current_i += 1
    return arr


def kth_smallest_elem(n, arr, k):
    arr = selection_sort(arr)
    return arr[k-1]


arr1 = np.array([7, 10, 4, 20, 15])
print(kth_smallest_elem(5, arr1, 4))

