"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

from math import sqrt

amicableSum = 0

def getDivisorsSum(number):
    divisors = [1]
    squareRoot = int(sqrt(number))+1

    for divisor in xrange(2, squareRoot):
        if number%divisor==0:
            divisors.append(divisor)
            divisors.append(number/divisor)

    return sum(set(divisors))



for num in xrange(10000, 1, -1):

    divisorSum = getDivisorsSum(num)

    if num == getDivisorsSum(divisorSum) and num != divisorSum:
        amicableSum += num

print amicableSum