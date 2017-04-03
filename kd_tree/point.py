# Define a 2d point for the node

# In case of empty constructor generate random number
from random import randint

# Define class
class Point:
    # Constructor
    def __init__(self, x=None, y=None):
        if x is None:
            x = randint(-100, 100)
        if y is None:
            y = randint(-100, 100)

        self.x = x
        self.y = y

    # Print
    def __str__(self):
        return "Point({}, {})".format(self.x, self.y)

    # Repr
    def __repr__(self):
        return str(self)
