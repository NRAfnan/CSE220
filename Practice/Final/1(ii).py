def fun(n):
    if n < 2:
        return 3
    return fun(n - 2) + 2 * fun(n - 4)


print(fun(5))
arr = [3, 1, 4, 2, 5]
print(arr[arr[arr[3]]])