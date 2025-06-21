num = int(input("Enter a number : "))

def InchToCm(n) :
    if(n == 0):
        return 0
    cm = n * 2.54
    return cm

res = InchToCm(num)

print(f"{num} Inch = {res} CM")