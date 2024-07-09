#this program will take a string and output the most common character in that string. If two or more characters appear the same amount of times, then they will be outputted in a comma separated list in the order they appear in the input string.
import sys

value1 = sys.argv[1]

stringList = []
charDict = {}

#creating a list of chars from the input string (space is omitted)
for char in value1:
    if char != " ":
        stringList.append(char)

#look through the input string and populate the alphabet dictionary with the number of times the character shows up
#this way, the dictionary will be in the order the chars appear in the string and the number of times they appear
for char in stringList:
    if char in charDict:
        charDict[char] += 1
    else:
        charDict[char] = 1

highestValueList = []

#find the highest value in the dictionary and add it to the highestValueList
highestValue = max(charDict.values())
for key in charDict:
    if charDict[key] == highestValue:
        highestValueList.append(key)

#output the highest value(s) in the order they appear in the string (comma separated if there are multiple)
for i in range(len(highestValueList)):
    if i == len(highestValueList) - 1:
        print(highestValueList[i])
    else:
        print(highestValueList[i], end = ",")