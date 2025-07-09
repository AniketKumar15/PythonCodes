# Object-Oriented Programming (OOP) in Python
# OOP is a programming paradigm that uses objects and classes to structure code. The concept focus on DRY (Don't Repeat Yourself) principle.
# Key concepts of OOP:
# 1. Class: A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
# 2. Object: An instance of a class. It contains data and methods defined by the class. Memory is Allocated when an object is created.
# Note : Object give the real world entity and class is a blueprint of that entity.
# Note 2 : Object of a class can invoke the methods, without revealing the implementation details of the methods. This is known as encapsulation and abstraction.

# Example of a class and object

class Student:
    name = "Default Name"
    age = 0
    grade = "Default Grade"
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")
    
    @staticmethod
    def greet():
        print("Hello, welcome to the Student class!")

# Creating an object of the Student class
student1 = Student()
# Setting attributes for the object
student1.name = "Aniket Kumar"
student1.age = 20
student1.grade = "A"
# Displaying the information of the student
student1.greet()  # Calling the static method
student1.display_info()

# Why we use self in the function within a class?
# The self parameter in a class method refers to the instance of the class itself. It allows access to the attributes and methods of the class within its own methods. Because we cant access the attributes and methods of the class without self unlike in c++ and java where we can access the attributes and methods of the class without self.

# New Note : Instance attributes take over the class attributes when they are defined in the object. This is known as instance variable shadowing. The instance variable will be used instead of the class variable.

# Now If a function dont take any object as an argument then it is called a static method. Static methods are not bound to the instance of the class and can be called without creating an object of the class. They are defined using the @staticmethod decorator. So we dont need to use self in the static method. Static methods are used when we want to perform some operation that is not related to the instance of the class.