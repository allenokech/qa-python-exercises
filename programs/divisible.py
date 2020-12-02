def divisible(a,b):
    if a % b == 0:
        return int(a / b)
    else:
        return f"{a} is not divisible by {b}"

print(divisible(5, 10)) #not divisible

print (divisible(10, 5)) # 2