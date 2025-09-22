# Write a Python program to add two positive integers without using the '+' operator. Note: Use bit wise operations to add two numbers.

def add_without_plus(a, b):
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

num1 = int(input("Enter first positive integer: "))
num2 = int(input("Enter second positive integer: "))

result = add_without_plus(num1, num2)
print("Sum:", result)
