"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

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


def rotateNumber(number):
    number = list(str(number))

    for x in xrange(0, len(number)-1):
        number.append(number.pop(0))

        yield int(''.join(number))


circularPrimes = {2:True}

for num in xrange(3,999999, 2):

    if num in circularPrimes:
        continue

    elif isPrimeNumber(num):
        isCircular = True
        cPrimes = [num]

        for rNum in rotateNumber(num):
            if rNum % 2 != 0 and isPrimeNumber(rNum):
                cPrimes.append(num)
            else:
                isCircular = False
                break

        if isCircular:
            for prime in cPrimes:
                circularPrimes[prime] = True

print len(set(circularPrimes))