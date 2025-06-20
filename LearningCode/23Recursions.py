# Recursions -> Recursion involves a function calling itself directly or indirectly to solve a problem by breaking it down into simpler and more manageable parts. 

def  Factorial(n):
    if(n == 0 or n == 1):
        return 1
    else :
        return n * Factorial(n-1)

res = Factorial(20)

print(f"Factorial of Number is : {res}")