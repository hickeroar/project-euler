"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91  99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

maxMain = 0

for x in xrange(999, 99, -1):
    for i in xrange(999, 99, -1):
        test = str(x * i)
        if len(test) % 2 == 0:
            left, right = test[0:(len(test)/2)], test[(len(test)/2):len(test)]
            right = right[::-1]
            if left == right:
                maxMain = max(maxMain, int(test))

print maxMain