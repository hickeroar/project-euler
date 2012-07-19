"""
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving
to the right and down, is indicated in bold red and is equal to 2427.

131 673 234 103 18
201 96  342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524 37  331

Find the minimal path sum, in http://projecteuler.net/project/matrix.txt, a 31K text file containing
a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
"""

matrix = []

matrixFile = open('solution081.txt', "r")
line = matrixFile.readline()

while line:
    matrix.append(map(int,line.split(',')))
    line = matrixFile.readline()

doneDict = {}

height = len(matrix)
width = len(matrix[0])

def testValue(row, column, total=0):

    dictKey = str(row)+'x'+str(column)

    if dictKey in doneDict:
        return doneDict[dictKey]

    testValues = []

    if row + 1 == height and column + 1 == width:
        return total + matrix[row][column]

    tests = []

    if column + 1 < width:
        tests.append([row, column+1])

    if row + 1 < height:
        tests.append([row+1, column])

    for r, c in tests:
        testValues.append(testValue(r, c, total))

    lowest = min(testValues)

    total += (matrix[row][column] + lowest)

    doneDict[dictKey] = total

    return total


print testValue(0, 0)
