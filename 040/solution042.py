"""
The nth term of the sequence of triangle numbers is given by, t(sub)n = 1/2n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values
we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle
number then we shall call the word a triangle word.

Find how many triangle words there are in the text file
"""
words = open('solution042.txt', "r").read().replace('"','').split(',')


wordValues = []

for word in words:
    wordValue = 0

    for letter in word:
        wordValue += (ord(letter) - 64)

    wordValues.append(wordValue)


triangleNumbers = {}
number = 0
maxWordValue = max(wordValues)

while True:
    number += 1

    value = int((0.5*float(number))*(number+1))

    triangleNumbers[value] = value

    if (value > maxWordValue):
        break


triangleWords = 0

for wordValue in wordValues:
    if wordValue in triangleNumbers:
        triangleWords += 1

print triangleWords