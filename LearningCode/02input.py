# In python, the input() function always returns a string, so if we want to take an integer input from the user, we need to typecast it to int, or if any other type, then we need explicit type casting.
a = input("Enter a number: ")
print(type(a)) # By default, string
a = int(a) # typecasting to int
print(a**2)

fName = input("Enter your first name: ")
lName = input("Enter your last name: ")
print("Hello " + fName + " " + lName)