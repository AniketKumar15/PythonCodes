# Map Funtion in python

def square(x):
    return x ** 2  

# Using map to apply the square function to a list of numbers
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# Filter Function in Python

def is_even(x):
    return x % 2 == 0

# Using filter to apply the is_even function to a list of numbers
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4]

# Reduce Function in Python
from functools import reduce

def multiply(x, y):
    return x * y

# Using reduce to apply the multiply function to a list of numbers
product = reduce(multiply, numbers)
print(product)  # Output: 120
