# List has many built-in functions
# append() – Adds an item to the end of the list
# extend() – Adds all elements of an iterable to the end of the list
# insert() – Inserts an item at a given position
# remove() – Removes the first occurrence of a specified value
# pop() – Removes and returns the item at the given position
# clear() – Removes all items from the list
# index() – Returns the index of the first matching item
# count() – Returns the number of occurrences of a value
# sort() – Sorts the list in ascending order (by default)
# reverse() – Reverses the elements of the list in place
# copy() – Returns a shallow copy of the list
# len() - Returns the number of items in the list
# max() - Returns the largest item in the list
# min() - Returns the smallest item in the list
# sum() - Returns the sum of all items in the list
# all() - Returns True if all items in the list are true
# any() - Returns True if any item in the list is true
# There are many more functions in list, but these are the most commonly used functions.

# Example of All functions
arr = [1,2,3,4,5]
arr1 = [7,8,9,10]
arr2 = [3,1,5,7,4,9,2,6,8,0]

arr.append(6)
print(arr)

arr.extend(arr1)
print(arr)

arr.insert(2, 11)
print(arr)

arr.remove(10)
print(arr)

valPop = arr.pop(2)
print(arr, valPop)


print(f"Value 3 present on the index -> {arr.index(3)}")
print(f"Value 3 Occurences -> {arr.count(3)}")

arr2.sort()
print(arr2)

arr.reverse()
print(arr)

arrNew = arr.copy()
print(arrNew)

print(f"Length of the list -> {len(arr)}")

print(f"Max value of the list -> {max(arr)}")
print(f"Min value of the list -> {min(arr)}")
print(f"Sum of the list -> {sum(arr)}")
print(f"All values are true -> {all(arr)}")
print(f"Any value is true -> {any(arr)}")

arr.clear()
print(arr)