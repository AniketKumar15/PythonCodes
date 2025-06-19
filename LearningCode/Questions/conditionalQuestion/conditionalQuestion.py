# Find greates from 4 numbers enter by the user

n1 = int(input("Enter first number : "))
n2 = int(input("Enter second number : "))
n3 = int(input("Enter third number : "))
n4 = int(input("Enter fourth number : "))
if(n1 == n2 == n3 == n4):
    print("All number are same")
elif (n1 > n2 and n1 > n3 and n1 > n4) : 
    print("N1 is greater")
elif (n2 > n1 and n2 > n3 and n2 > n4) :
    print("N2 is greater")
elif (n3 > n1 and n3 > n2 and n3 > n4) :
    print("N3 is greater")
elif (n4 > n1 and n4 > n2 and n4 > n3) :
    print("N4 is greater")
else : 
    print("Invalid Number")