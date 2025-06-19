# Write a program to find that the given name is present in the list or not.

usernameList = ["Aniket", "Rohit", "Sahil", "Amit", "Rahul"]

username = input("Enter your username: ")

if(username.capitalize() in usernameList) :
    print("Username is valid, you can login")
else:
    print("Username is not valid, Pls select from the list")