"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

[...CUT FOR BREVITY, SEE solution018.txt...]

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot
be solved by brute force, and requires a clever method! ;o)
"""

triangle = []

triangleFile = open('solution018.txt', "r")
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