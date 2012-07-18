"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total
from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in http://projecteuler.net/project/triangle.txt, a 15K text
file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem,
as there are 2^99 altogether! If you could check one trillion (10^12) routes every second it would take over twenty 
billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""


triangle = []

triangleFile = open('solution067.txt', "r")
line = triangleFile.readline()

while line:
    triangle.insert(0, map(int, line.split()))
    line = triangleFile.readline()


doneDict = {}

def testValue(row, column, total=0):

    dictKey = str(row)+'x'+str(column)

    if dictKey in doneDict:
        return doneDict[dictKey]

    highest = 0

    if row + 1 == len(triangle):
        return total + triangle[row][column]

    tests = []

    if column - 1 >= 0:
        tests.append(column-1)

    if column < len(triangle[row+1]):
        tests.append(column)

    for col in tests:
        result = testValue(row+1, col, total)
        if result > highest:
            highest = result

    total += (triangle[row][column] + highest)

    doneDict[dictKey] = total

    return total


highest = 0

for i in xrange(0, len(triangle[0])):
    
    result = testValue(0, i)

    if result > highest:
        highest = result

print highest