#!/usr/bin/env python3
import random
import argparse

# parse arguments
parser = argparse.ArgumentParser(description="Generate a secure, memorable password using the XKCD method")
parser.add_argument("-w", "--words", default=4, type=int, help="include WORDS in the password (default=4)")
parser.add_argument("-c", "--caps", default=0, type=int, help="capitalize the first letter of CAPS random words (default=0)")
parser.add_argument("-n", "--numbers", default=0, type=int, help="insert NUMBERS random numbers in the password (default=0)")
parser.add_argument("-s", "--symbols", default=0, type=int, help="insert SYMBOLS random symbols in the password (default=0)")
args = parser.parse_args()

numWords = args.words
numCaps = args.caps
numNums = args.numbers
numSymbs = args.symbols

# if number of words to be capitalized is greater than number of words, capitalize all words
if numCaps > numWords:
    numCaps = numWords

password = ""
theWordsList = []
accWordLengthsList = [0]
indWordLengthList = []
symbols = ["`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+",
              "=", "{", "}", "[", "]", "|", ";", ":", "<", ">", ",", ".", "?", "/", "'"]

# read in input file
with open('corncob_lowercase.txt') as inputfile:
    for line in inputfile:
        theWordsList.append(line.strip())
inputfile.close()

# select random words from dictionary
for x in range (0, numWords):
    newWord = random.choice(theWordsList)
    accWordLengthsList.append(len(newWord) + accWordLengthsList[-1])
    indWordLengthList.append(len(newWord))
    password = password + newWord
passwordAsList = list(password)
accWordLengthsList = accWordLengthsList[:-1]

# randomly capitalize the first letter of words in the password
if numCaps > 0:
    for y in range (0, numCaps):
        randomIndex = random.randint(0, (len(accWordLengthsList) - 1))
        newWordLength = accWordLengthsList.pop(randomIndex)
        theChar = passwordAsList[newWordLength]
        theChar = theChar.upper()
        passwordAsList[newWordLength] = theChar
password = ''.join(passwordAsList)

# randomly insert numbers into the password
if numNums > 0:
    for z in range (0, numNums):
        newNum = random.randint(0, 9)
        numPosition = random.randint(0, len(password))
        insertNum = password[:numPosition] + str(newNum) + password[numPosition:]
        password = insertNum

# randomly insert symbols into the password
if numSymbs > 0:
    for s in range (0, numSymbs):
        newSymb = random.choice(symbols)
        symbPosition = random.randint(0, len(password))
        insertSymb = password[:symbPosition] + newSymb + password[symbPosition:]
        password = insertSymb

print(password)
