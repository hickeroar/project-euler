"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from math import sqrt

def isPrimeNumber(number):
    for divisor in xrange(3, int(sqrt(number))+1, 2):
        if number % divisor == 0:
            return False
    return True

total = 2

for i in xrange(3, 2000000, 2):

    if isPrimeNumber(i):
        total += i

print total