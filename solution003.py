"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt

def isPrimeNumber(number):
    for divisor in xrange(3, int(sqrt(number))+1, 2):
        if number % divisor == 0:
            return False
    return True

def do(evilNumber, primeFactors=[]):

    if isPrimeNumber(evilNumber):
        primeFactors.append(evilNumber)
        return primeFactors

    divisor = 2
    evilNumber = float(evilNumber)

    while not evilNumber/divisor == int(evilNumber/divisor):
        divisor += 1

    return do(int(evilNumber/divisor), primeFactors) + do(divisor, primeFactors)


print max(do(600851475143))