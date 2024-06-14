import numpy as np


def find_frequency(n, arr, x):
    count = 0
    for elem in arr:
        if x == elem:
            count += 1
    return count


arr1 = np.ones(5, dtype=int)
n = 5
x = 1
print(find_frequency(n, arr1, x))