import numpy as np


def wave(n, arr):
    """
    1. Traverse if its even it should be greater than its next
    2. If its odd it should be lesser than its next
    3. Swap
    :param n: Size of the arr
    :param arr: numpy arr
    :return: wave like arr such that arr[1] >= arr[2] <= arr[3] >=arr[4] <= arr[5].....
    """
    i = 0
    while i < n - 1:
        if i % 2 == 0:
            # For even indices, ensure the current element is greater than the next one
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        else:
            # For odd indices, ensure the current element is lesser than the next one
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i += 1
    return arr


print('===Test Case 1===')
arr1 = np.array([1, 2, 3, 4, 5])
print(wave(5, arr1))

print('===Test Case 2===')
arr2 = np.array([2, 4, 7, 8, 9, 10])
print(wave(6, arr2))