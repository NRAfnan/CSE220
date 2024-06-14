def sumDigits(n):
    if 1 <= n <= 9:
        return n
    return n % 10 + sumDigits(n // 10)


print(sumDigits(12))