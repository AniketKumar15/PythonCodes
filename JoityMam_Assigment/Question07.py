# Write a Program to access element using tuple indexing, consider a tuple having 6 elements will have index from 0 to 5. Trying to access an element other than (6, 7,...) will raise an IndexError.

my_tuple = (10, 20, 30, 40, 50, 60)

try:
    print("Accessing element at index 2:", my_tuple[2])
    print("Accessing element at index 6:", my_tuple[6])  # out of range
except IndexError as e:
    print("Error:", e)
