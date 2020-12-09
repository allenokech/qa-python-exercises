def zipping(string1, string2):
    if len(string1) != len(string2):
        return "Not the same length"
    else:
        return "".join(i for j in zip(string1, string2) for i in j)

print(zipping("Dog", "Cat"))
