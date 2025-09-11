def is_prime(n):
    # Check if a number is prime.
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Get range input from user
start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))

print(f"Prime numbers between {start} and {end} are:")

for num in range(start, end + 1):
    if is_prime(num):
        print(num, end=" ")
