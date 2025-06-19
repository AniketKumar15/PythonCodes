# Range Function in Python 
# The range() function in Python is used to generate a sequence of numbers. It is commonly used in for loops to iterate over a sequence of numbers.
# The range() function can take one, two, or three arguments:
# 1. range(stop): Generates numbers from 0 to stop-1.
# 2. range(start, stop): Generates numbers from start to stop-1.
# 3. range(start, stop, step): Generates numbers from start to stop-1, incrementing by step.

for i in range(11):
    print(i, end=" ")
print("\n")

for i in range(5, 11):
    print(i, end=" ")
print("\n")

for i in range(5, 20, 3):
    print(i, end=" ")