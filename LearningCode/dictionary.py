# Dictionary in python is a collection of key value pairs.
# It is unordered, mutable and indexed.
# Dictionaries are defined using curly braces {}.

em = {} # Empty dictionary

marks = {
    "Aniket" : 90,
    "Rohit" : 85,
    "Harshit" : 89,
    "Yuvraj" : 95
}
print(marks["Aniket"])
print(marks["Rohit"])

# In Dictionary you can also make list inside it.
dic = {
    "test" : [1,2,4]
}
print(dic["test"][2]) # By this you can access the list particular element.