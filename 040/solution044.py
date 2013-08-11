"""
Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 - 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal 
    and D = |Pk - Pj| is minimised; what is the value of D?
"""

from sys import exit

pentNums = {1:1}
pentN = 1
maxPent = 1

def calcPent(n):
    newPent = (n*((3*n)-1))/2
    pentNums[newPent] = newPent
    return newPent

def isPent(n):
    global pentN, maxPent

    while maxPent < n:
        pentN += 1
        maxPent = calcPent(pentN)

    return n in pentNums

i = 1
while True:
    i += 1
    if isPent(i):
        for n in pentNums:
            if n == i:
                continue

            diff = i - n

            if diff in pentNums:
                
                if abs(diff-n) in pentNums:
                    print abs(diff-n)
                    exit()
                elif abs(n-diff) in pentNums:
                    print abs(n-diff)
                    exit()
