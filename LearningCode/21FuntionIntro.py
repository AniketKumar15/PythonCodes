# Python Functions is a block of statements that does a specific task. The idea is to put some commonly or repeatedly done task together and make a function so that instead of writing the same code again and again for different inputs, we can do the function calls to reuse code contained in it over and over again.

# Benefits of Using Functions
# - Code Reuse
# - Reduced code length
# - Increased readability of code

'''
Funtion Definition
def functionName(Parameters):
    # Function body
    # Code to be executed
    return value  # Optional return statement

Function Call
functionName(arguments)    
'''

def greet(name):
    print(f"Hello, {name}")

greet("Aniket Kumar")
greet("Rohit Kumar")


# -------- Function with Parameters and Return Value ---------------
def add(a, b):
    return a + b

result = add(5, 3)
print(f"The sum of 5 and 3 is: {result}")

# -------- Function with Default Parameters --------
def greet_with_default(name="Guest"):
    print(f"Hello, {name}")

greet_with_default()  # Calls with default parameter
greet_with_default("Alice")  # Calls with custom parameter

# -------- Function with Variable Number of Arguments --------
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4, 5)  # Can pass any number of arguments

# -------- Function with Keyword Arguments --------
def print_info(name, age):
    print(f"Name: {name}, Age: {age}")

print_info(name="Bob", age=30)  # Using keyword arguments

# -------- Function with Keyword Arguments and Default Values --------
def print_info_with_defaults(name="Unknown", age=0):
    print(f"Name: {name}, Age: {age}")

print_info_with_defaults()  # Calls with default values
print_info_with_defaults(name="Charlie")  # Calls with custom name, default age
print_info_with_defaults(age=25)  # Calls with custom age, default name


