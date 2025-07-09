# Class method -> A class method in Python is a method that is bound to the class itself, rather than to an instance of the class. It operates on the class as a whole and receives the class object as its first argument, conventionally named cls.

class TestClass:
    number = 100

    @classmethod
    def displayNumber(cls):
        print(f"Number is: {cls.number}")
    
    def displayInstanceNumber(self):
        print(f"Instance number is: {self.number}")

t1 = TestClass()
t1.number = 150
t1.displayNumber()  # Calls class method, will print 100
t1.displayInstanceNumber()  # Calls instance method, will print 150