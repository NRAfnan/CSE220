def count_x(str1, i):
    if i < 0:
        return 0
    if str1[i] == "x":
        return 1 + count_x(str1, i - 1)
    return 0 + count_x(str1, i - 1)


str1 = "hi"
print(count_x(str1, len(str1) - 1))