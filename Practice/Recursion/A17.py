def parenBit(given, i=0, got_left_paren=False):
    if i >= len(given):
        return ""

    if given[i] == "(":
        return given[i] + parenBit(given, i + 1, True)
    if given[i] == ")":
        return given[i]
    if got_left_paren:
        return given[i] + parenBit(given, i + 1, True)

    return parenBit(given, i + 1)


print(parenBit("xyz(abc)123"))
print(parenBit("x(hello)"))
print(parenBit("(xy)1"))