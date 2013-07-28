"""
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000
"""

digitcount = 0
current = 0
working = ''

while digitcount < 1000000:
    current += 1
    strCurrent = str(current)
    digitcount += len(strCurrent)
    working += strCurrent

result = 1

for x in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    result *= int(working[x-1])

print result