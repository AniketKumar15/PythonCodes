#Property decorator -> The @property decorator in Python is a built-in decorator that allows methods to be accessed like attributes, providing a "Pythonic" way to manage attribute access within a class. It simplifies the creation of managed attributes, offering control over how attribute values are retrieved, modified, and deleted, without requiring explicit calls to getter and setter methods.

class Person:
    @property
    def name(self):
        return self.ename
    
    @name.setter
    def name(self, value):
        self.fname = value.split()[0]
        self.lname = value.split()[1]
        self.ename = value
    
    def display(self):
        print(f"First Name: {self.fname}, Last Name: {self.lname}, Full Name: {self.ename}")


Person1 = Person()
Person1.name = "Aniket Kumar"
Person1.display()