# Constructor -> In python, a constructor is a special method that is automatically called when an object of a class is created. It is used to initialize the attributes of the class.
# Syntax: def __init__(self, parameters):

class Person:
    name = ""
    age = 0
    salary = 0.0
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")
    
# Creating an object of the Person class
p1 = Person("Aniket Kumar", 22, 500000.0)
p1.display()