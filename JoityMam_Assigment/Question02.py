# Write a program to count the number of even and odd numbers from a series of numbers. 
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

even_count = len([num for num in numbers if num % 2 == 0])
odd_count = len([num for num in numbers if num % 2 != 0])

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
