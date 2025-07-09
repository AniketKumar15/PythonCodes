# Operator overloading in Python allows the customization of how standard operators (like +, -, *, ==, etc.) behave when applied to instances of user-defined classes.

# This is achieved by implementing special methods, often referred to as "magic methods" or "dunder methods" (due to their double underscore prefix and suffix, e.g., __add__), within the class definition.

# __add__(self, other): For the + operator.
# __sub__(self, other): For the - operator.
# __mul__(self, other): For the * operator.
# __truediv__(self, other): For the / operator (true division).
# __floordiv__(self, other): For the // operator (floor division).
# __mod__(self, other): For the % operator.

# __eq__(self, other): For the == operator.
# __ne__(self, other): For the != operator.
# __lt__(self, other): For the < operator.
# __le__(self, other): For the <= operator.
# __gt__(self, other): For the > operator.
# __ge__(self, other): For the >= operator.

# __str__(self): For the str() function or print() function.
# __repr__(self): For the repr() function, which is used to get a string representation of the object that can be used for debugging.
# __len__(self): For the len() function, which returns the length of the object
# __getitem__(self, key): For indexing (e.g., obj[key]).
# __setitem__(self, key, value): For setting values using indexing (e.g, obj[key] = value).
# __delitem__(self, key): For deleting items using indexing (e.g., del obj[key]).

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(5, 7)
v3 = v1 + v2 # This will call the __add__ method
print(v3)  # Output: Vector(7, 10)