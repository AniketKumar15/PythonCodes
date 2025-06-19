num = int(input("Enter a number : "))

# Sum of N Natural number using For Loop
sum = 0
for i in range(1, num +1):
    sum += i
print(f"Sum of Natural Number is : {sum}")


# Sum of N Natural number using While Loop
sum = 0
i = 1
while(i <= num):
    sum += i
    i += 1
print(f"Sum of Natural Number is : {sum}")