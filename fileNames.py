#this program takes in a string of comma separated file names and outputs a string of the same file names with duplicates taken care of by adding a number in parentheses at the end of the duplicate file name (modeling the way windows handles duplicate file names)
import sys

value1 = sys.argv[1]

#sample input: "doc(3), doc(4), doc, doc, doc, doc, doc (6), (image ), hello world, helloworld, (image )(1), (image )"
#sample output: "doc(3), doc(4), doc, doc(1), doc(2), doc(5), doc (6), (image ), hello world, helloworld, (image )(1), (image )(2)"

#seperate the input string into a list of strings
stringList = value1.split(", ")

#dictionary to keep track of the number of times a file name has appeared
fileDict = {}
for i in range(len(stringList)):
    #if the file name is already in the dictionary, increment the value by 1
    if stringList[i] in fileDict:
        fileDict[stringList[i]] += 1
        #if the file name with the number in parentheses is already in the dictionary,
        if stringList[i] + "(" + str(fileDict[stringList[i]]) + ")" in fileDict:
            #keep adding 1 to the number in parentheses until it is not in the dictionary
            while stringList[i] + "(" + str(fileDict[stringList[i]]) + ")" in fileDict:
                fileDict[stringList[i]] += 1
            #finally, add the file name with this number to the dictionary
            stringList[i] = stringList[i] + "(" + str(fileDict[stringList[i]]) + ")"
        else:
            #if the file name with the number in parentheses is not in the dictionary, add it to the dictionary
            stringList[i] = stringList[i] + "(" + str(fileDict[stringList[i]]) + ")"
    
    #if the file name is not in the dictionary, add it to the dictionary with a value of 0
    else:
        fileDict[stringList[i]] = 0

#join the list of strings back together with a comma and space
print(", ".join(stringList))