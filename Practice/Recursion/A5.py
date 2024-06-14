def changePi(givenstr, i=0):
    if i < len(givenstr):
        if givenstr[i: i + 2] == "pi":
            return "3.14" + changePi(givenstr, i + 2)
        return givenstr[i] + changePi(givenstr, i + 1)
    return ""


print(changePi("xxpi"))
print(changePi("pipi"))
print(changePi("pip"))