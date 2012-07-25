"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier,
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

from itertools import permutations
import sys

products = []
numlist = ['1','2','3','4','5','6','7','8','9']

for num in permutations(numlist):

    for x in xrange(1, 3):
        operand1 = ''.join(num[0:x])
        oLen = len(operand1)
        operand1 = int(operand1)
        operand2 = int(''.join(num[x:x+5-oLen]))

        product = int(''.join(num[5:]))

        if operand1 * operand2 == product:
            products.append(product)

print sum(set(products))