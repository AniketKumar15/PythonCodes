# Write a program to compute distance between two points taking input from the user (Pythagorean Theorem)

import math

x1, y1 = map(float, input("Enter coordinates of first point (x1 y1): ").split())
x2, y2 = map(float, input("Enter coordinates of second point (x2 y2): ").split())

distance = math.hypot(x2 - x1, y2 - y1)
print("Distance between points:", distance)
