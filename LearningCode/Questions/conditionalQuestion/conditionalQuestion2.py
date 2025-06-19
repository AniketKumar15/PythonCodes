marks1 = int(input("Enter Your marks : "))
marks2 = int(input("Enter Your marks : "))
marks3 = int(input("Enter Your marks : "))

total_percentage = (100 * (marks1 + marks2 + marks3)) / 300

if (marks1 > 100 or marks2 > 100 or marks3 > 100) : 
    print("Every Subject Marks must be within 100")
elif (marks1 < 33 or marks2 < 33 or marks3 < 33) : 
    print("You are Failed becuase you get less than 33% in subject")
elif (total_percentage >= 40) : 
    print("You passed away with :",round(total_percentage , 2),"%")
else :
    print("You failed, Go and sleep Because you get only",round(total_percentage , 2),"%")