# 1.1 Computational concerns for algorithms
# Listing 1.2: Linear search to find point in a list

# Initialize distance to a very large number
mindist = 10000000000

# Initialize empty lists for points
l = []
m = []

# Fill the list l with data by appending
for x in range (1,100,2):
    for y in range (1,100,3):
        l.append((x,y))

# Fill the list m with data
for x in range (1,100,3):
    for y in range (1,100,2):
        m.append((x,y))

# Go through the lists and calculate distances between points
for pointl in l:
    for pointm in m:
        if pointl != pointm:
            # calculate distance
            if d < mindist:
                mindist = d

print(mindist)
