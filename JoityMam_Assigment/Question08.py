# Write a program to access a range of items in a tuple by using the slicing operator colon ":"

my_tuple = (10, 20, 30, 40, 50, 60)

print("Accessing elements from index 1 to 4:", my_tuple[1:4])
print("Accessing elements from index 2 to end:", my_tuple[2:])
print("Accessing elements from start to index 3:", my_tuple[:3])
print("Accessing all elements:", my_tuple[:])
print("Accessing elements with step 2:", my_tuple[::2])
print("Accessing elements in reverse order:", my_tuple[::-1])