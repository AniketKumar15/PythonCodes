# write a program to calculate the grade of student based on the given scheame

marks = int(input("Enter your marks out of 100: "))

if(marks < 0 or marks > 100):
    print("Invalid marks, please enter a value between 0 and 100.")
    exit()

if(marks <= 100 and marks >= 90):
    grade = "Ex"
elif(marks < 90 and marks >=80):
    grade = "A"
elif(marks < 80 and marks >= 70):
    grade = "B"
elif(marks < 70 and marks >= 60):
    grade = "C"
elif(marks < 60 and marks >= 50):
    grade = "D"
elif(marks < 50):
    grade = "F"

print(f"Your grade is: {grade}")

