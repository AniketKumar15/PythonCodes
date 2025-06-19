# Break -> break keyword is used to break the flow of the loop and exit the loop.
# Continue -> Continue keyword is used to skip the current iteration of the loop and continue with the next iteration.
# Pass -> Pass keyword is used to do nothing. It is a null operation. It is used when a statement is required syntactically but you do not want any command or code to execute.

# Pass Example
for i in range(10):
    pass

# Break Example
for i in range(10):
    if i == 5:
        break
    print(i, end=" ")

#continue Example
print("\n")
for i in range(10):
    if i == 5:
        continue
    print(i, end= " ")

