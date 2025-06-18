# Type casting in python
# it is a process of converting one data type into another like int to float.
# it has two types: implicit(automatic) and explicit (manual).
# implicit type casting done by python itself. 
# Explicit type casting need to be done manual by the programmer, The function use to convert are int(), float(), str(), bool() etc.
# Note : Type casting is not possible between all data types. For example, you cannot convert a string that contains letters into an integer.
# Note : In Explicit type casting, in some cases, the data may be lost. For example, if you convert a float to an int, the decimal part will be truncated. like 3.14 will be converted to 3, so 0.14 will be lost, that may be important in some cases, so be careful while using explicit type casting.

# implicit type Casting 

# Python automatically converts 
# a to int 
a = 7
print(type(a)) 

# Python automatically converts 
# b to float 
b = 3.0
print(type(b)) 

# Explicit type casting

c="32"
print(type(c))
# typecast to int
d = int(c)
print(type(d))