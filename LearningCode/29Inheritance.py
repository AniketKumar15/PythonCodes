# Inheritance -> Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called a child or derived class) to inherit attributes and methods from another class (called a parent or base class). This promotes code reuse, modularity, and a hierarchical class structure. 

class Human :  #-> This is the parent class/base class/super class
    def display(self):
        print("I am a human being")
    def walk(self):
        print("I can walk")

class Student(Human): #-> This is the child class/derived class/sub class
    def study(self):
        print("I am studying")


Student1 = Student()
Student1.display()  # Inherited method from Human class
Student1.walk()    # Inherited method from Human class
Student1.study()   # Method from Student class