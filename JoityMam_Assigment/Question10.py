# Consider a list (sample_list = []). You can perform the following commands:
# Read 5 integer elements append in list
# Insert 5 at 0th position
# print: Print the list.
# Delete the first occurrence of even integer.
# print: Print the list.
# Insert 27 at the end of the list
# print: Print the list.
# Sort the list.
# print: Print the list.
# Pop the last element from the list.

# Step 1: Create an empty list
sample_list = []

# Step 2: Read 5 integers from user and append to the list
print("Enter 5 integers:")
for _ in range(5):
    num = int(input())
    sample_list.append(num)

# Step 3: Insert 5 at the 0th position
sample_list.insert(0, 5)

# Step 4: Print the list
print("After inserting 5 at 0th position:", sample_list)

# Step 5: Delete the first occurrence of an even integer
for num in sample_list:
    if num % 2 == 0:
        sample_list.remove(num)
        break  # only the first occurrence
# Print the list
print("After deleting first even number:", sample_list)

# Step 6: Insert 27 at the end of the list
sample_list.append(27)

# Step 7: Print the list
print("After appending 27:", sample_list)

# Step 8: Sort the list
sample_list.sort()

# Step 9: Print the list
print("After sorting the list:", sample_list)

# Step 10: Pop the last element from the list
popped_element = sample_list.pop()

# Step 11: Print final list and the popped element
print("After popping the last element:", sample_list)
print("Popped element:", popped_element)
