#this program takes in two inputs, the first is a fibonacci number and the second is the number of fibonacci numbers you want to print after the first input and prints the list of fibonacci numbers after the first input


import sys

value1 = int(sys.argv[1])
value2 = int(sys.argv[2])


#find out how many fibonacci numbers you need
#create list of fibonacci numbers as you do this
fibMinusTwo = 0
fibMinusOne = 1
fibList = [0, 1]

fibCurrent = 1

while fibCurrent != value1:
    fibCurrent = fibMinusTwo + fibMinusOne
    fibMinusTwo = fibMinusOne
    fibMinusOne = fibCurrent
    fibList.append(fibCurrent)
#length of desired list
length = len(fibList) + value2
#add the rest of the fibonacci numbers to the list
if(len(fibList) >= 2):
    while len(fibList) != length:
        fibList.append(fibList[-1] + fibList[-2])

newList = []
#go through the list, find the number that matches the first input and then continue to add the rest of the numbers to the list
for i in range(len(fibList)):
    if fibList[i] == value1:
        newList = fibList[i+1:]
        break

#print list of numbers with commas and no brackets
print(','.join(map(str, newList)))