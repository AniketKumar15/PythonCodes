num = int(input("Enter a number : "))

def SumOfN(n):
   if(n == 0) :
       return 0
   else :     
        return n + SumOfN(n - 1)

    
res = SumOfN(num)

print(f"{res}")