#Sets in Python are unordered collections of unique, immutable elements. They are defined using curly braces {} or the set() constructor. Sets are mutable, allowing the addition and removal of elements, but they cannot contain duplicate values.

# sets can define by four ways:

# 1. Using curly braces {}
mySet = {1, 2, 3, 4, 5, 4, 4, 3}
print(type(mySet))
print(mySet) # {1, 2, 3, 4, 5} - duplicate values are removed

# 2. Using set() constructor
mySet1 = set([1, 2, 3, 4, 5, 4, 4, 3])
print(type(mySet1))
print(mySet1) # {1, 2, 3, 4, 5} - duplicate values are removed

# 3. Using set() constructor with string
mySet2 = set("Hello")
print(type(mySet2))
print(mySet2) # {'H', 'e', 'l', 'o'} - duplicate values are removed

# 4. Using set() constructor with tuple
mySet3 = set((1, 2, 3, 4, 5, 4, 4, 3))
print(type(mySet3))
print(mySet3) # {1, 2, 3, 4, 5} - duplicate values are removed

# 5. Using set() constructor with list
mySet4 = set([1, 2, 3, 4, 5, 4, 4, 3])
print(type(mySet4))
print(mySet4) # {1, 2, 3, 4, 5} - duplicate values are removed

# 6. Using set() constructor with dictionary
mySet5 = set({1: "one", 2: "two", 3: "three"})
print(type(mySet5))
print(mySet5) # {1, 2, 3} - only keys are added to the set

# 7. Using set() constructor with dictionary
mySet6 = set({1: "one", 2: "two", 3: "three"}.values())
print(type(mySet6))
print(mySet6) # {'one', 'two', 'three'} - only values are added to the set

# 8. Using set() constructor with dictionary
mySet7 = set({1: "one", 2: "two", 3: "three"}.items())
print(type(mySet7))
print(mySet7) # {(1, 'one'), (2, 'two'), (3, 'three')} - only items are added to the set
