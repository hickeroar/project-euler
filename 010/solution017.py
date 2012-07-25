"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there
are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

textNumbers = {
    0:'',
    1:'one',
    2:'two',
    3:'three',
    4:'four',
    5:'five',
    6:'six',
    7:'seven',
    8:'eight',
    9:'nine',
    10:'ten',
    11:'eleven',
    12:'twelve',
    13:'thirteen',
    14:'fourteen',
    15:'fifteen',
    16:'sixteen',
    17:'seventeen',
    18:'eighteen',
    19:'nineteen',
    'tens':{
        2:'twenty',
        3:'thirty',
        4:'forty',
        5:'fifty',
        6:'sixty',
        7:'seventy',
        8:'eighty',
        9:'ninety',
    }
}

def getSingleDigitText(x):

    if int(x) in textNumbers:
        return textNumbers[int(x)]

def getDoubleDigitText(x):

    if int(x) in textNumbers:
        return textNumbers[int(x)]

    return textNumbers['tens'][int(x[0])] + getSingleDigitText(int(x[1]))

def getTripleDigitText(x):

    text = getSingleDigitText(int(x[0])) + 'hundred'
    tens = getDoubleDigitText(x[1:3])

    if tens:
        text = text + 'and' + tens

    return text

numberString = ''

for x in xrange(1, 1001):
    x = str(x)

    thisNum = None

    if len(x) == 1:
        thisNum = getSingleDigitText(x)

    elif len(x) == 2:
        thisNum = getDoubleDigitText(x)

    elif len(x) == 3:
        thisNum = getTripleDigitText(x)

    else:
        thisNum = 'onethousand'

    numberString += thisNum

print len(numberString)