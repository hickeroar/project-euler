"""
See solution026-1.py for problem explanation.

References:
    http://mathworld.wolfram.com/DecimalExpansion.html
    http://mathworld.wolfram.com/MultiplicativeOrder.html

Rules (from references):
    1) The number of digits in the repeating portion of the decimal expansion of a rational number can also be found directly from the multiplicative order of its denominator.
    2) The multiplicative order of 10 mod an integer n relatively prime to 10 gives the period of the decimal expansion of the reciprocal of n.
    3) Any nonregular fraction m/n is periodic, and has a period lambda(n) independent of m, which is at most n-1 digits long.
"""

def getDecimalPeriod(n):
    for x in xrange(2, n):
        if pow(10, x, n) == 1: # Multiplicative order of 10 mod i to find x, Rule #2
            return x

for n in xrange(999, 3, -2): # Odd only (relatively prime to 10). Rule #2 
    if 5 % n == 0: # Mod 5 != 0 only (relatively prime to 10). Rule #2 
        continue
                
    if n-1 == getDecimalPeriod(n):
        # n-1 is the highest possible number, and we're
        # on the highest possible number that has it. Rule #3
        break

print n