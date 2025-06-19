# Write a program to print a table of given numbe by the user.

num = int(input("Enter a number : "))

print(f"Table of {num} using For loop:")
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")


# Same with while loop
i = 1
print(f"\nTable of {num} using While loop:")
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1