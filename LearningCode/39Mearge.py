# New operators | and |= allow for merging and updating dictionaries.

dict1 = {'a': 1, 'b': 4}
dict2 = {'b': 3, 'c': 4}
dict3 = {'b': 5, 'a': 6, 'd': 7}

# Merging dictionaries using the | operator
merged_dict = dict1 | dict2
print("Merged Dictionary:", merged_dict)

# Updating dictionaries using the |= operator
dict1 |= dict3
print("Updated Dictionary 1:", dict1)