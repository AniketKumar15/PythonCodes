# Write a program that the given username contains less than 10 characters or not.

username = input("Enter your username: ")

if(len(username) < 10):
    print("Username is valid")
else:
    print("Username is not valid, it should be less than 10 characters")