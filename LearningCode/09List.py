# List in python is also called array, we all know that array is a collection of similar type of data in contiguous memory location.
# In python, list is a collection of different types of data in contiguous memory location.
# List is mutable, means we can change the value of list.
# List slicing is same as string slicing

arr = [1,2,3,4,5] # Valid list
arr1 = [1,2.4,4.2,"Aniket", True] # Valid list

# List can access by index that start from 0
print(arr[0])
print(arr1[3])

# We can change the value of list
print(arr[2])
arr[2] = 10
print(arr[2])

print(arr[-2]) # -2 means second last element
print(arr[1:4]) # 1 to 4 index
print(arr[1:]) # 1 to last index
print(arr[:4]) # 0 to 4 index
print(arr[1:4:2])
print(arr[::2]) # 0,10,5 index
print(arr[::-1]) # reverse the list
