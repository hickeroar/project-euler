"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

import operator

squareDict = {}
squares = []
successes = {}

for x in xrange(1, 1001):
    square = x**2
    squares.append(square)
    squareDict[square] = x

for i in xrange(999, -1, -1):
    for lower in xrange(i-1, ((i-1)/2), -1):

        a = squares[i] - squares[lower]
        if a in squareDict:
            perimeter = squareDict[a] + squareDict[squares[i]] + squareDict[squares[lower]]

            if perimeter <= 1000:
                if perimeter in successes:
                    successes[perimeter] += 1
                else:
                    successes[perimeter] = 1

print max(successes.iteritems(), key=operator.itemgetter(1))[0]