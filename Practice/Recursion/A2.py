def check(n):
    if n % 2 == 0:
        return 3
    return 2


def bunnyEars2(n):
    if n == 0:
        return 0
    return check(n) + bunnyEars2(n - 1)


def bunnyEars2(n):
    if n == 0:
        return 0
    if n == 1:
        return 2
    if n == 2:
        return 3 + bunnyEars2(n - 1)
    return bunnyEars2(n - 1) + bunnyEars2(n - 2)


print(bunnyEars2(2))