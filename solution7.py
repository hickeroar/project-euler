"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

def isPrimeNumber(number):
    for divisor in xrange(3, number/2, 2):
        if number % divisor == 0:
            return False

    return True

primes = [2]
i = 3
numPrimes = 1

while numPrimes < 10001:
    if isPrimeNumber(i):
        primes.append(i)
        numPrimes += 1
    i += 2

print max(primes)