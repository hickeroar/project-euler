"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def isEvenlyDivisible(num):
    for i in range(20, 0, -1):
        if num % i != 0:
            return False

    return True

solution = None
testNum = 2520

while True:
    if isEvenlyDivisible(testNum):
        solution = testNum
        break
    else:
        testNum += 2520

print solution