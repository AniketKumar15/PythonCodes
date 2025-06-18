# In python, dictionary has many built-in functions.
# some of them are: 
# item() - Returns a list of tuples containing the key value pairs.
# keys() - Returns a list of all the keys in the dictionary.
# values() - Returns a list of all the values in the dictionary.
# get() - Returns the value of the specified key.
# update() - Updates the dictionary with the specified Key value pair.
# pop() - Removes the element with the specified key.
# popitem() - Removes the last inserted key value pair.
# clear() - Removes all the elements from the dictionary.
# copy() - Returns a shallow copy of the dictionary.
# len() - Returns the lenght of the dictionary.

marks = {
    "Aniket" : 90,
    "Rohit" : 85,
    "Harshit" : 89,
    "Yuvraj" : 95
}
print(len(marks))
print(max(marks, key = marks.get), max(marks.values())) # max will give the key with maximum value.
print(min(marks, key = marks.get), min(marks.values())) # min will give the key with minimum value.
print(max(marks))
print(min(marks))

print(type(marks))
print(marks)
print(marks["Aniket"])
print(marks.items())
print(marks.keys())
print(marks.values())
print(marks.get("Rohit"))

marks.update({"Rohit" : 58})
print(marks)
marks.update({"Rohit" : 58, "Anjani" : 56}) # if we update any key value pair that not exist then it will add that key value pair.
print(marks)

print(dict(sorted(marks.items())))
print(dict(sorted(marks.items(), key = lambda item: item[1]))) 

# Negative sorting also work

# What is diffrence between marks.items("Aniket") and marks["Aniket"] ? 
# marks.items(), if in case the key is not present then it will not give error but it will return empty none.
# Whereas marks["Aniket"] will give error if the key is not present in the dictionary.


marks.pop("Rohit")
print(f"After pop Rohit ->  {marks}")
newMarks = marks.copy()
print(f"New Copy of marks -> {newMarks}")

marks.popitem()
print(f"After popitem -> {marks}")


# replace 
# Replace key "Aniket" with "Rohan"
marks["Rohan"] = marks.pop("Aniket")
print(marks)

marks.clear()
print(f"After clear -> {marks}")