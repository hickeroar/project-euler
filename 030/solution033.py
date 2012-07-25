"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify
it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value,
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

from fractions import Fraction

final = 1

for d in [a for a in xrange(11, 99) if a % 10 != 0]:
    denominator = list(str(d))
    for n in [b for b in xrange(11, d) if b % 10 != 0]:
        numerator = list(str(n))

        orig = float(n)/float(d)

        inter = set(numerator).intersection(set(denominator))

        for i in inter:
            onum = list(numerator)
            oden = list(denominator)
            onum.remove(i)
            oden.remove(i)
            new = float(''.join(onum))/float(''.join(oden))

            if new == orig:
                final *= orig

print Fraction(str(final))