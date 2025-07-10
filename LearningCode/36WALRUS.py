# Walrus Operator -> The walrus operator (:=), introduced in Python 3.8, allows you to assign values to variables as part of an expression. This operator, named for its resemblance to the eyes and tusks of a walrus, is officially called the "assignment expression."

def walrus_operator_example():
    # Using the walrus operator to assign a value to a variable within an expression
    if (n := 10) > 5:
        print(f"The value of n is {n} and it is greater than 5.")
    else:
        print(f"The value of n is {n} and it is not greater than 5.")

walrus_operator_example()