# 2.6 Intersection of two line segments
# Listing 2.7: Calculating the intersection between two line segments

# Imports
import math
from geometries.point import *

def pip_cross(point, pgon):
    """
    Determines whether a point is in a polygon.
    Code adopted from the C program in Graphics Gems IV by Haines (1994).
    Input:
        pgon: a list of points as the vertices for a polygon
        point: the point
    Output:
        Returns a boolean value of True or False and the number of times the half-line crosses the polygon boundary
    """
