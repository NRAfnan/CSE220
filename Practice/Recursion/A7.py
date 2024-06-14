def pairStar(given, i=0):
    if i >= len(given):
        return ""
    if given[i: i + 2] == given[i] * 2:
        return given[i] + "*" + pairStar(given, i + 1)
    return given[i] + pairStar(given, i + 1)


print(pairStar("hello"))

print(pairStar("xxyy"))

print(pairStar("aaaa"))