def count11(arr, i):
    if i >= len(arr):
        return 0
    if arr[i] == 11:
        return 1 + count11(arr, i + 1)
    return 0 + count11(arr, i + 1)


arr = [1, 2, 3, 4]
print(count11(arr, 0))