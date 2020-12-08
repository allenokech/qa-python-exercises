def calcCase(myString):
    upper_count = 0
    lower_count = 0
    for i in myString:
        if i.isupper():
            upper_count+=1
    for i in myString:
        if i.islower():
            lower_count+=1
    return f"UPPER CASE {upper_count}\nLOWER CASE {lower_count}"

myString = str(input("Enter phrase: "))
print(calcCase(myString))
