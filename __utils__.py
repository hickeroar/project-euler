"""
Utilities for use in euler problems
"""

# Prime Numbers
from math import sqrt
primes = {}
def isPrimeNumber(number):
    if number in primes:
        return True
    for divisor in xrange(3, int(sqrt(number))+1, 2):
        if number % divisor == 0:
            return False
    primes[number] = True
    return True

# Divisors
from math import sqrt
def getDivisors(number):
    divisors = [1]
    for divisor in xrange(2, int(sqrt(number))+1):
        if number%divisor==0:
            divisors.append(divisor)
            divisors.append(number/divisor)
    return set(divisors)
