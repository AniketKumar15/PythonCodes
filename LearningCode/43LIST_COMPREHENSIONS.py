# List Comprehensions
# List comprehensions provide a concise way to create lists.

squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# List comprehensions can also include conditions.
evens = [x**2 for x in range(20) if x % 2 == 0]
print(evens)  # Output: [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]

# Nested list comprehensions can be used for multi-dimensional lists.
matrix = [[j for j in range(3)] for i in range(3)]
print(matrix)  # Output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]