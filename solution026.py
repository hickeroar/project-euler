"""
A unit fraction contains 1 in the numerator.
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""


from decimal import Decimal, getcontext
"""from math import sqrt

def isPrimeNumber(number):
    for divisor in xrange(3, int(sqrt(number))+1, 2):
        if number % divisor == 0:
            return False
    return True
"""

precision = 2000
getcontext().prec = precision

winningNumber = 0
winningLength = 0

for d in xrange(2, 1001):

    #if not isPrimeNumber(d):
    #    continue

    testVal = str(Decimal(1)/Decimal(d))

    if len(testVal) < precision+2:
        continue

    testVal = testVal.rstrip('0')

    checkLength = 3
    repLength = None

    while checkLength < (precision-1)/2:
        if testVal[-checkLength-1:-1] == testVal[-checkLength-1-checkLength:-1-checkLength]:
            repLength = checkLength
            break
        checkLength += 1

    if None == repLength:
        raise Exception("Precision is inadequate. Raise it!")

    if repLength > winningLength:
        winningNumber = d
        winningLength = repLength

print winningNumber