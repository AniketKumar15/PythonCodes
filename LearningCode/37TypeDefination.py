# Type hints are added using the colon (:) syntax for variables and the -> syntax for function return types.
# Python's typing module provides more advanced type hints, such as List, Tuple, Dict, and Union.


n : int = 10
a : float = 10.5
s : str = "Hello, World"
print (f"n: {n}, a: {a}, s: {s}")

def add(x : int, y : int) -> int:
    return x + y

sum = add(5, 10)
print(f"Sum: {sum}")

from typing import List, Tuple, Dict, Union

numbers : List[int] = [1, 2, 3, 4, 5]
coordinates : Tuple[float, float] = (10.5, 20.5)
user_info : Dict[str, Union[str, int]] = {"name": "Alice", "age": 30}

print(f"Numbers: {numbers}")
print(f"Coordinates: {coordinates}")
print(f"User Info: {user_info}")