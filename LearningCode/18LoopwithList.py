# Loop with List, Tuple, String, Dictionary, Set

# 1. Loop With List
li = ["Aniket", "Rohit", "Sahil", "Amit", "Rahul"]
for i in li:
    print(i, end = " ")
print("\n")

# 2. Loop With Tuple
tup = ("Aniket", "Rohit", "Sahil", "Amit", "Rahul")
for i in tup:
   print(i, end = " ")
print("\n")

# 3. Loop With String  
s = "Geeks"
for i in s:
    print(i, end= "")
print("\n")

# 4. Loop With Dictionary
d = dict({'x':123, 'y':354})
for i in d:
    print("%s  %d" % (i, d[i]))
print("\n")
    
# 5. Loop With Set
set1 = {1, 2, 3, 4, 5, 6}
for i in set1:
    print(i, end=" ")