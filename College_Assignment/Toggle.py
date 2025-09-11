s = input("Enter a string: ")
s1 = ""
for char in s: 
    ascii_val = ord(char)
    # Only flip letters, ignore others
    if 65 <= ascii_val <= 90 or 97 <= ascii_val <= 122:
        s1 += chr(ascii_val ^ 32)  # XOR 32 flips case
    else:
        s1 += char

print("Toggled string:", s1)


# s = input("Enter a string: ")

# s1 = ""
# for char in s:
#     ascii_val = ord(char)
#     # Check if uppercase A-Z
#     if 65 <= ascii_val <= 90:
#         # Convert to lowercase by adding 32
#         s1 += chr(ascii_val + 32)
#     # Check if lowercase a-z
#     elif 97 <= ascii_val <= 122:
#         # Convert to uppercase by subtracting 32
#         s1 += chr(ascii_val - 32)
#     else:
#         # Leave other characters unchanged
#         s1 += char

# print("Toggled string:", s1)
