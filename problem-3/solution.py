"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def isPrimeNumber(number):
    number = float(number)

    for divisor in xrange(2, int(round(number/2))):

        if number/divisor == int(number/divisor):
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