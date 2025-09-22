# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
# Note: String letters are case-sensitive.
# Sample Input
# ABCDCDC CDC
# Sample Output
# 2

# Read input
string = input("Enter the main string: ")
substring = input("Enter the substring: ")

count = 0
for i in range(len(string) - len(substring) + 1):
    if string[i:i+len(substring)] == substring:
        count += 1

print(count)
