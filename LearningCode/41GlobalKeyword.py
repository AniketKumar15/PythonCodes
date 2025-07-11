# Global Keyword
# The 'global' keyword is used to modify the variable outside of the current scope.

x = 10

def modify_global():
    global x
    x = 20

modify_global()
print(x)  # Output: 20