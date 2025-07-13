# Lambda Expression is a small anonymous function that can take any number of arguments, but can only have one expression.
# It is often used for short, throwaway functions that are not reused elsewhere.

add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

square = lambda x: x ** 2
print(square(4))  # Output: 16

addMany = lambda *args: sum(args)
print(addMany(1, 2, 3, 4, 5))  # Output: 15