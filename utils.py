"""
Utilities for use in euler problems
"""

# Prime Numbers
from math import sqrt
primes = {}
nonPrimes = {}
def isPrimeNumber(number):
    if number in primes:
        return True
    if number in nonPrimes:
        return False
    for divisor in xrange(3, int(sqrt(number))+1, 2):
        if number % divisor == 0:
            nonPrimes[number] = True
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
