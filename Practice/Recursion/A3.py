def check7(n):
    if n == 7:
        return 1
    return 0


def count7(n):
    if n == 0:
        return 0
    return check7(n % 10) + count7(n // 10)





print(count7(717))
print(count7(7))
print(count7(0))