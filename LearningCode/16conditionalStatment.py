# Conditional statements in Python allow you to control the flow of your program
# based on different conditions. They let your program make decisions.
# The basic types of conditional statements are:
# 1. if        - Executes a block of code if the condition is True
# 2. elif      - Checks another condition if the previous ones are False
# 3. else      - Executes a block if none of the above conditions are True

# Conditional statements can be written like this:

# 1. Basic if statement
num = 11
if num > 0:
    print("Positive number")  # Output: Positive number

# 2. if-else statement
num = -5
if num >= 0:
    print("Non-negative")
else:
    print("Negative")  # Output: Negative

# 3. if-elif-else ladder
num = 0
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")  # Output: Zero
else:
    print("Negative")

#This is if else code