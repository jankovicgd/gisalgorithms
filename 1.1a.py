
l = []

for x in range (30,50,5):
    for y in range (1,10,3):
        l.append((x,y))

print(l)

p = (31, 1)

print(p)

for point in l:
    if point == p:
        print("Found point")
