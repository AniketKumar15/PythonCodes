# Q1. Write a program to create a dictionary of hindi words with values as their englist translation. Provide user with an option to look it up.

# meaningWord = {
#     "Ajnabi" : "Stranger",
#     "Bachpan" : "Childhood",
#     "Chand" : "Moon",
#     "Dost" : "Friend",
#     "Ekta" : "Unity",
#     "Fikr" : "Worry"
# }

# print("Welcome to Hindi to English Dictionary")
# word = input("Enter the word you want to search: ")
# print(f"The meaning of {word} is {meaningWord.get(word, 'not found')}")


# Q1 Ended


# Q2. Write a program to input eight number from the user and display all the unique numbers(once).

# numbers = set()

# n = input("Enter the number - ")
# numbers.add(int(n))
# n = input("Enter the number - ")
# numbers.add(int(n))
# n = input("Enter the number - ")
# numbers.add(int(n))
# n = input("Enter the number - ")
# numbers.add(int(n))
# n = input("Enter the number - ")
# numbers.add(int(n))
# n = input("Enter the number - ")
# numbers.add(int(n))
# n = input("Enter the number - ")
# numbers.add(int(n))
# n = input("Enter the number - ")
# numbers.add(int(n))

# print(f"The unique numbers are {numbers}")

# Q2 Ended


# Q3 Can we have a set with 18(int) and 18(str) as a value?
# set1 = {18, "18"}
# print(type(set1))
# print(set1)

# Yes it is possible.
# Q3 Ended


#Q4. What is length of set? 

# set2 = set()
# set2.add(20)
# set2.add(20.0)
# set2.add("20")

# print(f"The length of set is {len(set2)}")

# Lenght of set is 2 because 20 and 20.0 are same value although they are different data types.
# Q4 Ended


# Q5. Type of s what ? 
# s = {}
# print(type(s))

# It is a dictionary not set, becuase it is empty dictionary.
# Q5 Ended


# Q6. Write a program to input 5 friend name and there favirot programming language in the dictionary

# d = {}

# name = input("Enter Your name : ")
# lang = input("Enter programming language : ")
# d.update({name : lang})
# name = input("Enter Your name : ")
# lang = input("Enter programming language : ")
# d.update({name : lang})
# name = input("Enter Your name : ")
# lang = input("Enter programming language : ")
# d.update({name : lang})
# name = input("Enter Your name : ")
# lang = input("Enter programming language : ")
# d.update({name : lang})
# name = input("Enter Your name : ")
# lang = input("Enter programming language : ")
# d.update({name : lang})

# print(d)

# Q6 Ended


# Q7. Can you update it [1,2] inside set?
se = {8, 7, 12, "Aniket", [1,2]}  
# ❌ This will cause an error because [1,2] is a list, and lists are unhashable (can't be added to a set)
