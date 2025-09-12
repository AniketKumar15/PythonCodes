s = input("Enter a string: ")

# Remove spaces from the string
s1 = ""
for char in s:
    if char != ' ':
        s1 += char

print("String without spaces:", s1)