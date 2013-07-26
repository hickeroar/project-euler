"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

from math import sqrt

counts = {}

for x in xrange(1000, 0, -1):
    maxInt = float(x**2)

    