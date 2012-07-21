"""
In England the currency is made up of pound and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, 1 pound (100p) and 2 pound (200p).

How many different ways can 2 pounds` be made using any number of coins?
"""

numbers = [1,2,5,10,20,50,100,200]
counts = [0]*(max(numbers)+1)

counts[0] = 1

for num in numbers:
    for i in xrange(num, len(counts)):
        counts[i] += counts[i-num]

print max(counts)