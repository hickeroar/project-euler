"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written
as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater
than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced
any further by analysis even though it is known that the greatest number that cannot be expressed as the sum
of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

from math import sqrt

abundantNumbers = []

abundantSum = 0


def getDivisorSum(number):
    divisors = [1]
    squareRoot = int(sqrt(number))+1

    for divisor in xrange(2, squareRoot):
        if number%divisor == 0:
            divisors.append(divisor)
            divisors.append(number/divisor)

    return sum(set(divisors))


def canAbundantSum(number):

    for x in abundantNumbers:
        if (number-x) in abundantNumbers:
            return True

    return False


for i in xrange(28123, 0, -1):

    if getDivisorSum(i) > i:
        abundantNumbers.append(i)

abundantNumbers = set(abundantNumbers)

for i in xrange(28123, 0, -1):

    if not canAbundantSum(i):
        abundantSum += i

print abundantSum