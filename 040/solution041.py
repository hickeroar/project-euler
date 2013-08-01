"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

from sys import exit
from math import sqrt
from itertools import permutations

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

for i in xrange(9, 4, -1):
    currentString = ''
    for x in xrange(i, 0, -1):
        currentString += str(x)
    for x in permutations(currentString):
        working = int(''.join(x))
        if working % 2 != 0 and isPrimeNumber(working):
            print working
            exit()
