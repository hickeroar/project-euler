"""
The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.
"""

sumOfNums = 0
sumOfSquares = 0

for i in xrange(0, 101):
    sumOfNums += i
    sumOfSquares += i**2

print (sumOfNums**2-sumOfSquares)