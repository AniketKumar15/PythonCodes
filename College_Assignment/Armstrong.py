# Program to check if a number is Armstrong

num = int(input("Enter a number: "))

# convert number to string to easily get digits
digits = str(num)
power = len(digits)

# calculate sum of each digit raised to the power
total = sum(int(digit) ** power for digit in digits)

# check condition
if total == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")
