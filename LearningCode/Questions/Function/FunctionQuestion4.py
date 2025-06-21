num = int(input("Enter a number : "))

def Pattern(n):
    if(n == 0):
        return
    print("*" * n)
    Pattern(n-1)

Pattern(num)