a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))
c = int(input("Enter Third Number : "))

def GreatestNumber(x,y,z):
    if(x == y == z):
        print("All are Same!")
    else:
        if(x > y and x > z):
            return x
        elif(y > x and y > z):
            return y
        else:
            return z

res = GreatestNumber(a,b,c)

if(res != None):
    print(f"{res} is Greatest")