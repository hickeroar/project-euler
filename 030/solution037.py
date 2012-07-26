"""
The number 3797 has an interesting property. Being prime itself, it is possible to continuously
remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly
we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from math import sqrt
primes = {}
nonPrimes = {}
def isPrimeNumber(number):
    if number == 1:
        return False
    if number % 2 == 0 and number != 2:
        return False

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

interestingPrimes = []
currentTest = 11

while True:
    
    passesTheTest = True

    i = currentTest
    while i:
        if not isPrimeNumber(i):
            passesTheTest = False
            break
        i /= 10

    if passesTheTest:
        i = int(str(currentTest)[1:] or 0)
        while i:
            if not isPrimeNumber(i):
                passesTheTest = False
                break
            i = int(str(i)[1:] or 0)

    if passesTheTest:
        interestingPrimes.append(currentTest)
        if len(interestingPrimes) == 11:
            break

    currentTest += 2

print sum(interestingPrimes)