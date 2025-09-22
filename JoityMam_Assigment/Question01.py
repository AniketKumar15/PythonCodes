# Write a program to find those number which are divisible by 8 and multiple of 5, between 100 and 600 (both included).

result = []
for num in range(100, 601):
    if num % 8 == 0 and num % 5 == 0:
        result.append(num)

print("Numbers divisible by 8 and multiple of 5 between 100 and 600:")
for n in result:
    print(n, end=" ")