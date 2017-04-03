from kd_node import *

# pts = []
# for i in range(7):
#     pts.append(Point())

pts =[Point(6,7), Point(4,6), Point(9,4), Point(2,3), Point(3,7), Point(7,4), Point(9,6)]
print(str(pts))

root = kd_node(p=pts[0])
kd_tree = kd_tree(root)

for p in pts[1:]:
    kd_tree.add_point(p)

print(str(kd_tree))