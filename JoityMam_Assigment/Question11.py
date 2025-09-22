# You have a record of N students. Each record contains the student's name, and their percent marks in Maths, Physics and Chemistry. The marks can be floating values. The user enters some integer N followed by the names and marks for N students. You are required to save the record in a dictionary data type. The user then enters a student's name. Output the average percentage marks obtained by that student, correct to two decimal places.


def Enter_student_data(student_records):
    n = int(input("How many students do you want to add? "))
    for _ in range(n):
        name = input("Enter student's name: ").strip()
        maths = float(input("Enter Maths marks: "))
        physics = float(input("Enter Physics marks: "))
        chemistry = float(input("Enter Chemistry marks: "))
        student_records[name] = {
            "Maths": maths,
            "Physics": physics,
            "Chemistry": chemistry
        }
        print(f"Record added for {name}.")

def Print_All_Records(student_records):
    if student_records:
        print("\n--- All Student Records ---")
        for name, marks in student_records.items():
            print(f"{name}: {marks}")
    else:
        print("No records found.")

def Find_Student_Average(student_records):
    query_name = input("Enter the student's name to query: ").strip()
    found = False
    for name in student_records:
        if name.lower() == query_name.lower():
            marks = student_records[name]
            average = (marks["Maths"] + marks["Physics"] + marks["Chemistry"]) / 3
            print(f"Average percentage marks for {name}: {average:.2f}")
            found = True
            break
    if not found:
        print("Student not found.")


def main():
    student_records = {}
    
    while True:
        print("\n--- Student Record System ---")
        print("1. Add Student Records")
        print("2. View All Records")
        print("3. Find Student Average")
        print("0. Exit")
        
        choice = input("Enter your choice: ").strip()
        
        match choice:
            case "1":
                Enter_student_data(student_records)
            
            case "2":
                Print_All_Records(student_records)

            case "3":
                Find_Student_Average(student_records)
            
            case "0":
                print("Exiting... Goodbye!")
                break
            
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()