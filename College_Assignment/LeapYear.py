# Program to check if a year is a leap year

year = int(input("Enter a year: "))

# A year is a leap year if:
# 1. It is divisible by 400, OR
# 2. It is divisible by 4 but not divisible by 100
if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(year, "is a Leap Year.")
else:
    print(year, "is not a Leap Year.")
