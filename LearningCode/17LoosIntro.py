# Loops In python -> Loops in Python are used to repeat actions efficiently. 
# There are two main types of loops in python :
    # 1. For Loop
    # 2. While Loop

# For Loop in Python
# For loops are used for sequential traversal. For example: traversing a list or string or array etc. In Python, there is "for in" loop which is similar to foreach loop in other languages

# While Loop in Python :
# In Python, a while loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the line immediately after the loop in the program is executed.

# For Loop Ex -
for i in range(0, 11):
    print(i, end= " ")

print("\n")


# While Loop Ex -
cnt = 0
while (cnt <= 10):
    print(cnt, end= " ")
    cnt += 1

# use else with while loop
print("\n")
i = 0
while (i <= 5):
    print(i, end= " ")
    i += 1
else:
    print("\nElse block executed, i is now:", i)

