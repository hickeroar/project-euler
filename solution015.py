"""
Starting in the top left corner of a 2x2 grid, there are 6 routes (without backtracking) to the bottom right corner.

Image: http://projecteuler.net/project/images/p_015.gif

How many routes are there through a 20x20 grid?
"""

from math import factorial

gridWidth = 20
gridHeight = 20

numerator = factorial(gridWidth+gridHeight)
denominator = factorial(gridWidth)*factorial(gridHeight)

print numerator/denominator