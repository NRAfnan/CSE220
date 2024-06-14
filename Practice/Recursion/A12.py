def triangle(n):
    if n == 0:
        return n
    return n + triangle(n - 1)


print(triangle(2))