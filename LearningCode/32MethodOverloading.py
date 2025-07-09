# Method Overloading -> In python, method overloading is not supported directly.
# However, we can achieve method overloading by using default arguments or variable-length arguments.

class MathOperations:
    def add(self, a, b=0, c=0):
        """Adds two or three numbers."""
        return a + b + c

    def multiply(self, a, b=1, c=1):
        """Multiplies two or three numbers."""
        return a * b * c
    def display(self, *args):
        """Displays all arguments passed to the method."""
        for arg in args:
            print(arg)

# Example usage
math_ops = MathOperations()
print(math_ops.add(5, 10))
print(math_ops.add(5, 10, 15))
print(math_ops.multiply(5, 10))
print(math_ops.multiply(5, 10, 2))
math_ops.display("Hello", "World", 123)
