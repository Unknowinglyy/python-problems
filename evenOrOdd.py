#this program adds the digits that make up a number and determines if that sum is even or odd.
import sys

value1 = int(sys.argv[1])

intList = []
sum = 0

#seperate the digits contained in the number
while value1 != 0:
    intList.append(value1 % 10)
    value1 = value1 // 10

#iterate through the list of digits and sum them
for i in range(len(intList)):
    sum += intList[i]

#determine if sum is even or odd 
if sum % 2 == 0:
    print("even")
else:
    print("odd")