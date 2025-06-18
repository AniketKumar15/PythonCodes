# Tuple in Python
# A tuple is a collection which is ordered and immutable.
# Tuples are similar to lists, but unlike lists, once a tuple is created, it cannot be modified (i.e., no append(), remove(), etc.).
# Tuples are defined using parentheses ().

# Commonly used functions and operations with tuples:
# index() – Returns the index of the first matching item
# count() – Returns the number of occurrences of a value
# len() – Returns the number of items in the tuple
# max() – Returns the largest item in the tuple
# min() – Returns the smallest item in the tuple
# sum() – Returns the sum of all items in the tuple (if numeric)
# all() – Returns True if all items in the tuple are true
# any() – Returns True if any item in the tuple is true
# Tuple can also be used for unpacking
# Tuples support slicing and iteration

# Example of common tuple functions
tup = (1, 2, 3, 4, 5, 3, 2)

print(f"Original Tuple: {tup}")

# index()
print(f"Index of value 3 -> {tup.index(3)}")

# count()
print(f"Occurrences of value 2 -> {tup.count(2)}")

# len()
print(f"Length of the tuple -> {len(tup)}")

# max()
print(f"Maximum value in the tuple -> {max(tup)}")

# min()
print(f"Minimum value in the tuple -> {min(tup)}")

# sum()
print(f"Sum of all values in the tuple -> {sum(tup)}")

# all()
print(f"All values are true -> {all(tup)}")

# any()
print(f"Any value is true -> {any(tup)}")

# Tuple unpacking
a, b, c, d, e, f, g = tup
print(f"Unpacked values: {a}, {b}, {c}, {d}, {e}, {f}, {g}")

# Slicing
print(f"Sliced tuple (index 2 to 5) -> {tup[2:6]}")

# concatenation
tup2 = (6,7,8)
newTup = tup + tup2
print(f"Concatenated tuple -> {newTup}")
print(f"Concatenated tuple (with itself) -> {tup + tup}")

# Iteration
print("Iterating over tuple:")
for item in tup:
    print(item, end=' ')
