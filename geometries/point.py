# 2.1 Point
# Listing 2.1: Data structure for a point class

# Import sqrt from math library
from math import sqrt

# Define a class for points
class Point():
    # Constructor defines points
    def __init__(self, x = None, y = None):
        self.x, self.y = x, y

    # Get function that takes coordinates
    def __getitem__(self, i):
        if i == 0:
            return self.x
        if i == 1:
            return self.y
        return None

    # Function of length - because 2 dimensions always 2
    def __len__(self):
        return 2

    # Check whether two points are equal
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    # Check whether two points are not equal
    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return result
        return not result

    # Check whether the point is less than an other point
    def __lt__(self, other):
        if isinstance(other, Point):
            if self.x < other.x:
                return True
            elif self.x == other.x and self.y < other.y:
                return True
            return False
        return NotImplemented

    # Check whether the point is greater than an other point
    def __gt__(self, other):
        if isinstance(other, Point):
            if self.x > other.x:
                return True
            elif self.x == other.x and self.y > other.y:
                return True
            return False
        return NotImplemented

    # Check whether the point is greater than or equal an other point
    def __ge__(self, other):
        if isinstance(other, Point):
            if self.x >= other.x:
                return True
            elif self.x == other.x and self.y >= other.y:
                return True
            return False
        return NotImplemented

    # Check whether the point is less than or equal an other point
    def __le__(self, other):
        if isinstance(other, Point):
            if self.x <= other.x:
                return True
            elif self.x == other.x and self.y <= other.y:
                return True
            return False
        return NotImplemented

    # String
    def __str__(self):
        if type(self.x) is int and type(self.y) is int:
            return "({0}, {1})".format(self.x, self.y)
        else:
            return "({0:.1f}, {1:.1f})".format(self.x, self.y)

    # Repr
    def __repr__(self):
        if type(self.x) is int and type(self.y) is int:
            return "({0}, {1})".format(self.x, self.y)
        else:
            return "({0:.1f}, {1:.1f})".format(self.x, self.y)

    # Euclidean distance function
    def distance(self, other):
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    # Manhattan distance
    def mandistance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)
