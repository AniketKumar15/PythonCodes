# Type of Inheritance: 
# 1. Single Inheritance: A class inherits from one parent class.
# 2. Multiple Inheritance: A class inherits from multiple parent classes. 
# 3. Multilevel Inheritance: A class inherits from another class, which in turn inherits from another class.
# 4. Hierarchical Inheritance: Multiple classes inherit from a single parent class.
# 5. Hybrid Inheritance: A combination of two or more types of inheritance.


# 1. Single Inheritance
class Animal:  # Parent class
    def speak(self):
        print("Animal speaks")

class Dog(Animal):  # Child class
    def bark(self):
        print("Dog barks")

# Creating an object of the Dog class
dog = Dog()
dog.speak()  # Inherited method from Animal class
dog.bark()   # Method from Dog class


# 2. Multiple Inheritance
class Bird:  # First parent class
    def fly(self):
        print("Bird flies")

class Bat:  # Second parent class
    def hang(self):
        print("Bat hangs upside down")

class FlyingFox(Bird, Bat):  # Child class
    def forage(self):
        print("Flying fox is foraging")

# Creating an object of the FlyingFox class
flying_fox = FlyingFox()
flying_fox.fly()    # Inherited method from Bird class
flying_fox.hang()   # Inherited method from Bat class
flying_fox.forage() # Method from FlyingFox class

# 3. Multilevel Inheritance
class Vehicle:  # Grandparent class
    def start(self):
        print("Vehicle starts")

class Car(Vehicle):  # Parent class
    def drive(self):
        print("Car drives")

class SportsCar(Car):  # Child class
    def accelerate(self):
        print("Sports car accelerates rapidly")

# Creating an object of the SportsCar class
sports_car = SportsCar()
sports_car.start()      # Inherited method from Vehicle class
sports_car.drive()      # Inherited method from Car class
sports_car.accelerate() # Method from SportsCar class
