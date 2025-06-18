# In python String is a sequence of characters, so we can use indexing to access the characters in the string. The index starts from 0, so the first character is at index 0, the second character is at index 1, and so on. We can also use negative indexing to access the characters from the end of the string. The last character is at index -1, the second last character is at index -2, and so on.
# String is inmutable, means we we chanege the string, it will create a new string instead of changing the original string. So, we cannot change the original string.

text = "HELLO"
# The characters and their positive indexes are:
print(text[0])  # Output: H
print(text[1])  # Output: E
print(text[4])  # Output: O

# The characters and their negative indexes are:
print(text[-1])  # Output: O (last character)
print(text[-2])  # Output: L (second last)
print(text[-5])  # Output: H (first character)



# | Character | Index |
# | --------- | ----- |
# | H         | 0     |
# | E         | 1     |
# | L         | 2     |
# | L         | 3     |
# | O         | 4     |

# | Character | Negative Index |
# | --------- | -------------- |
# | H         | -5             |
# | E         | -4             |
# | L         | -3             |
# | L         | -2             |
# | O         | -1             |

# f sting  -> f-string is a way to format strings in Python. It is a more readable and concise way to format strings compared to the older methods like str.format() or % formatting. f-strings are available in Python 3.6 and later versions.
name = "Aniket Kumar"
print(f"Hello Mr, {name}")
print("Hello Mr,",name) # Without f-string
print("Hello Mr, " + name) # Without f-string


