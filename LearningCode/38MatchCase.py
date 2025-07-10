# Match Case -> Python 3.10 introduced the match statement, which is similar to the switch statement found in other programming languages. 

def match_case_example(value):
    match value:
        case 1:
            return "You selected option 1."
        case 2:
            return "You selected option 2."
        case 3:
            return "You selected option 3."
        case _:
            return "Invalid option."
        

n = int(input("Enter a number (1-3): "))
if(n < 1 or n > 3):
    print("Invalid input. Please enter a number between 1 and 3.")
else:
    result = match_case_example(n)
    print(result)