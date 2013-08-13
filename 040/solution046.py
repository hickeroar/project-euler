"""
It was proposed by Christian Goldbach that every odd composite (non prime)
number can be written as the sum of a prime and twice a square.

9 = 7 + 2x1^2
15 = 7 + 2x2^2
21 = 3 + 2x3^2
25 = 7 + 2x3^2
27 = 19 + 2x2^2
33 = 31 + 2x1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

from math import sqrt
primes = {2:True, 3:True}
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


squareNum = 1
maxTS = 1
twiceSquares = [2]
def nextTwiceSquare():
    global squareNum, maxTS
    squareNum += 1
    maxTS = 2*(squareNum**2)
    twiceSquares.append(maxTS)
    return maxTS


def testProof(odd, prime):
    global maxTS
    while maxTS < (odd + prime):
        nextTwiceSquare()
    for x in twiceSquares:
        if prime + x == odd:
            return True
    return False


odd = 3
proof = True
while proof:
    odd += 2
    if not isPrimeNumber(odd):
        proof = False
        for prime in primes:
            if testProof(odd, prime):
                proof = True
                break

print odd