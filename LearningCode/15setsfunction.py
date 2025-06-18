# Set Functions Covered:
# 1. add() - Adds an element to the set
# 2. update() - Adds multiple elements to the set
# 3. remove() - Removes a specified element from the set
# 4. discard() - Removes a specified element from the set (does not raise an error if not found)
# 5. pop() - Removes and returns an arbitrary element from the set
# 6. clear() - Removes all the elements from the set
# 7. union() - Returns the union of two sets
# 8. intersection() - Returns the intersection of two sets
# 9. difference() - Returns the difference of two sets
# 10. symmetric_difference() - Returns the symmetric difference of two sets
# 11. issubset() - Checks if a set is a subset of another set
# 12. issuperset() - Checks if a set is a superset of another set
# 13. isdisjoint() - Checks if two sets have no elements in common
# 14. copy() - Returns a shallow copy of the set

# Sample sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Note: you can find len(), max(), min(), sum(), all(), any()
print("\n1. len():")
print(f"set1 length: {len(set1)}")

print("\n1. max():")
print(f"set1 max: {max(set1)}")

print("\n1. min():")
print(f"set1 min: {min(set1)}")

print("\n1. sum():")
print(f"set1 sum: {sum(set1)}")

print("\n1. all():")
print(f"set1 all: {all(set1)}")

print("\n1. any():")
print(f"set1 any: {any(set1)}")

# You can also sort the set, but it will return a list so we need to convert it back to set
setNew = {2,1,6,5,7,0,8}
print(set(sorted(setNew)))

# 1. add()
print("\n1. add():")
set1.add(10)
print(f"set1 after add(10): {set1}")

# 2. update()
print("\n2. update():")
set1.update([11, 12])
print(f"set1 after update([11, 12]): {set1}")

# 3. remove()
print("\n3. remove():")
set1.remove(10)  # Will raise KeyError if not present
print(f"set1 after remove(10): {set1}")

# 4. discard()
print("\n4. discard():")
set1.discard(99)  # Won't raise an error if not found
print(f"set1 after discard(99): {set1}")

# 5. pop()
print("\n5. pop():")
popped = set1.pop() # Could be 1,2,3,11,12 — unpredictable!
print(f"Popped item: {popped}")
print(f"set1 after pop(): {set1}")

# 6. clear()
print("\n6. clear():")
temp_set = {100, 200}
temp_set.clear()
print(f"temp_set after clear(): {temp_set}")

# Resetting set1 for further examples
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 7. union()
print("\n7. union():")
print(f"set1 union set2: {set1.union(set2)}")

# 8. intersection()
print("\n8. intersection():")
print(f"set1 intersection set2: {set1.intersection(set2)}")

# 9. difference()
print("\n9. difference():")
print(f"set1 difference set2: {set1.difference(set2)}")

# 10. symmetric_difference()
print("\n10. symmetric_difference():")
print(f"set1 symmetric_difference set2: {set1.symmetric_difference(set2)}")

# 11. issubset()
print("\n11. issubset():")
subset_check = {1, 2}
print(f"{subset_check} is subset of set1: {subset_check.issubset(set1)}")

# 12. issuperset()
print("\n12. issuperset():")
print(f"set1 is superset of {subset_check}: {set1.issuperset(subset_check)}")

# 13. isdisjoint()
print("\n13. isdisjoint():")
disjoint_check = {10, 20}
print(f"set1 is disjoint with {disjoint_check}: {set1.isdisjoint(disjoint_check)}")

# 14. copy()
print("\n14. copy():")
set_copy = set1.copy()
print(f"Copy of set1: {set_copy}")
