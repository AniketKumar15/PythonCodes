# Exception handling in Python is a way to gracefully handle errors that may occur during the execution of a program. It allows you to catch and respond to exceptions, preventing the program from crashing.

# Exception handling is done using the try and except blocks.

# Exception is an error that occurs during the execution of a program. When an exception occurs, Python stops executing the current block of code and jumps to the nearest exception handler.

# We can use multiple except blocks to handle different types of exceptions. This allows us to provide specific error messages or take different actions based on the type of exception that occurred.

result = None

try: 
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a/b
    
except ZeroDivisionError as e:
    print("Error: Division by zero is not allowed.", e)
except Exception as e:
    print("An error occurred:", e)
else:
    print("The result is:", result)
    print("No exceptions were raised.")
finally:
    print("This block always executes, regardless of whether an exception occurred or not.")

# we can also use the `else` block to execute code that should run if no exceptions were raised in the try block. The `finally` block can be used to execute code that should run regardless of whether an exception occurred or not.

# The `finally` block is useful for cleanup actions, such as closing files or releasing resources, that should always be executed.