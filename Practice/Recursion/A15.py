def endX(given, i=0):
    if i >= len(given):
        return ""
    if given[i] != "x":
        return given[i] + endX(given, i + 1)
    return endX(given, i + 1) + given[i]


print(endX("xxre"))
print(endX("xxhixx"))
print(endX("xhixhixhix"))