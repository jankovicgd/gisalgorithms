# 1.1 Computational concerns for algorithms
# Listing 1.1: Linear search to find point in a list

# Initialize an empty list for points
l = []

# Fill the list l with data by appending
for x in range (30,50,5):
    for y in range (1,10,3):
        l.append((x,y))

# Test print
print(l)

# The point searched for
p = (30, 1)

# Search for the point in a list
for point in l:
    if point == p:
        print("Found point")
