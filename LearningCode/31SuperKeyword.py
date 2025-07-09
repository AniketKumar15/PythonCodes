# Super Keyword -> In python, the super() function is used to call a constructor or method of a parent class from a child class. It allows you to access inherited methods that have been overridden in a child class. This is particularly useful when you want to extend the functionality of a parent class method in a child class.

class Human:  # Parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Human):  # Child class
    def __init__(self, name, age, grade):
        super().__init__(name, age)  # Calling the constructor of the parent class
        self.grade = grade

    def display(self):
        super().display()  # Calling the display method of the parent class
        print(f"Grade: {self.grade}")

# Creating an object of the Student class
student = Student("Aniket Kumar", 22, "A")
student.display()