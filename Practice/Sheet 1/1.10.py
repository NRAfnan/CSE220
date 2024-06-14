import numpy as np


def count_jumps_required(n, arr):
    """
    1. We traverse if we find 0 and we did not traverse the whole arr return -1
    2. Otherwise, We traverse for an amount of each value is in the list
    :param n: size of the given arr
    :param arr: numpy arr
    :return: The number of jumps required to finish the arr traversal or - 1 if we could not traverse
    """
    i = 0
    jumps = 0
    while i < n - 1:
        if arr[i] == 0:
            return -1
        else:
            i += arr[i]
            jumps += 1
    return f"Jumps: {jumps}"


arr1 = np.array([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9])
print(count_jumps_required(11, arr1))
arr2 = np.array([1, 4, 3, 2, 6, 7])
print(count_jumps_required(6, arr2))
# n = 6
# i = 0
# jumps = 0
# while i < n - 1:
#     if arr2[i] == 0:
#         print(-1)
#     else:
#         i += arr2[i]
#         jumps += 1
# print(f"Jumps: {jumps}")
