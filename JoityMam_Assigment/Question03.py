# Write a python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the number that are divisible by 4 in a comma separated sequence.

binary_numbers = input("Enter comma separated 4 digit binary numbers: ").split(',')
divisible_by_4 = []

for binary in binary_numbers:
    if len(binary) == 4 and all(bit in '01' for bit in binary):
        decimal_value = int(binary, 2)
        if decimal_value % 4 == 0:
            divisible_by_4.append(binary)

print("Numbers divisible by 4:", ','.join(divisible_by_4))