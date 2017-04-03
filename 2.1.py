# 2.1 Point
# Listing 2.1 - run file to test the Point

# Import the point class from geometries
from geometries.point import *

# Define points a and b
a = Point(1, 2)
b = Point(5, 3)

# Print point a
print(a)

# Print results of logcal operations between a and b
print(b > a)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

# Print length of a
print(len(a))

# Print distance between a and b
print(a.distance(b))
