# 1.1 Computational concerns for algorithms
# Listing 1.2: Linear search to find point in a list

# Import mathematical functions
from math import *

# Initialize distance to a very large number
mindist = 10000000000

# Initialize empty lists for points
l = []
m = []

# Fill the list l with data by appending
for x in range (1, 10, 2):
    for y in range (1, 10, 3):
        l.append((x,y))

# Fill the list m with data
for x in range (34, 45, 4):
    for y in range (37, 50, 3):
        m.append((x,y))

# Print to make sure that everything is in order
print(l)
print(m)
print(len(l))
print(len(m))

# Go through the lists and calculate distances between points
for pointl in l:
    for pointm in m:
        if pointl != pointm:
            d = sqrt(pow((pointl[0] - pointm[0]), 2) + pow((pointl[1] - pointm[1]), 2))
            if d < mindist:
                mindist = d

# Print final result
print(mindist)
