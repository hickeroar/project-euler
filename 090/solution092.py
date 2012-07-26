"""
A number chain is created by continuously adding the square of the digits in a number to form a new 
number until it has been seen before.

For example,

44 -> 32 -> 13 -> 10 -> 1 -> 1
85 -> 89 -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. 
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

def primeCache(ones, eightynines):

    for x in xrange(567, 1, -1):

        if x in ones or x in eightynines:
            continue

        nums = []
        curNum = x
        found = False

        while not found:

            nums.append(curNum)

            if curNum == 1:
                found = True
                for n in nums:
                    ones[n] = True
                break

            if curNum == 89:
                found = True
                for n in nums:
                    eightynines[n] = True
                break

            workNum = curNum
            curNum = 0

            while workNum:
                digit = (workNum % 10)**2
                curNum += digit
                workNum /= 10

ones = {}
eightynines = {}

primeCache(ones, eightynines)

total89s = 0

for x in xrange(9999999, 1, -1):

    workNum = x
    var = 0

    while workNum:
        digit = (workNum % 10)**2
        var += digit
        workNum /= 10

    if var in eightynines:
        total89s += 1

print total89s