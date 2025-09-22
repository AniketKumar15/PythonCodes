# Write a program to find number whose sum of digits is largest using key function

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

numbers = [123, 456, 789, 12, 34]
largest = max(numbers, key=sum_of_digits)

print("Number with largest sum of digits:", largest)
