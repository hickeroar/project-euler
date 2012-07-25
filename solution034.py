"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

from math import factorial

eqSum = 0

factorials = {
    9:factorial(9),
    8:factorial(8),
    7:factorial(7),
    6:factorial(6),
    5:factorial(5),
    4:factorial(4),
    3:factorial(3),
    2:factorial(2),
    1:factorial(1),
    0:factorial(0)
}

for num in xrange(3,factorials[9]*7):
    workNum = num
    workSum = 0

    while workNum:
        digit = workNum % 10
        workSum += factorials[digit]
        workNum /= 10

    if workSum == num:
        eqSum += workSum

print eqSum