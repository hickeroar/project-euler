"""
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

palSum = 0

for num in xrange(1, 1000000):
    strNum = str(num)
    if strNum == strNum[::-1] and bin(num)[2:] == bin(num)[:1:-1]:
        palSum += num

print palSum