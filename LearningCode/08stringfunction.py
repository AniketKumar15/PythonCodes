# String Functions -> string has many built-in functions to manipulate strings.
# Some of the most commonly used string functions are:
# len() -> returns the length of the string
# string.endwith() -> returns true if the string ends with the specified substring, otherwise it returns fales
# lower() -> returns the string in lowercase
# upper() -> returns the string in uppercase
# title() -> returns the string in title case (first letter of each word is capitalizesd)
# capitalize() -> returns the string in capitalized case (first letter of the string is capitalized)
# swapcase() -> returns the string in swapcase (lowercase becomes uppercase and uppercase becomes lowercase
# find() -> returns the index of the first occurrence of the substring in the string. if the substring is not found, it returns -1
# strip() -> removes any leading and trailing whitespace characters from the string
# replace(old, new) -> replaces all occurences of the specified substring with the specified substring
# count() -> returns the number of occurrences of the specified substring in the string
# isalpha() -> returns true if all characters in the string are alphabets, otherwise it returns false
# isdigit() -> returns true if all characters in the string are digits, otherwise it returns false
# isalnum() -> returns true if all characters in the string are alphanumeric, otherwise it returns false
# isspace() -> returns true if all characters in the string are whitespace characters, otherwise it returns false
# islower() -> returns true if all characters in the string are lowercase, otherwise it returns false
# isupper() -> returns true if all characters in the string are uppercase, otherwise it returns false
# istitle() -> returns true if the string is in title case, otherwise it returns false
# split() -> splits the string into a list of substrings based on the specified delimiter


name = "aniket kumar"
string3 = "   hello world   "
print(len(name))
print(name.endswith("e"))
print(name.startswith("an"))
print(name.lower())
print(name.upper())
print(name.title())
print(name.capitalize())
print(name.swapcase())
print(name.find("k"))
print(name.find("z"))
print(string3.strip())
print(string3.rstrip())
print(string3.lstrip())

print(name.replace("a", "A"))
print(name.count("a"))
print(name.isalpha())
print(name.isdigit())
print(name.isalnum())
print(name.isspace())
print(name.islower())
print(name.isupper())
print(name.istitle())
print(name.split())

text = "43"
print(text.zfill(5)) # Output: 00043
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
print(txt1)
print(txt2)
print(txt3)