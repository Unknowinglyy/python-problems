#this program takes in a number and recursively sums the digits of that number until the sum is only one digit long

import sys

value1 = int(sys.argv[1])

#function to seperate the digits of a number and return them in a list
def seperateDigits(num: int):
    digitList = []
    while num > 0:
        digitList.append(num % 10)
        num = num // 10
    return digitList

#function to sum the digits of a list and if that sum is greater than 9, call the function again
def recursiveSum(list: list):
    sum = 0
    #find sum of the list of digits
    for i in list:
        sum += i
    #if that sum is at least 2 digits long, call the function again
    if sum > 9:
        return recursiveSum(seperateDigits(sum))
    #once the sum is only one digit long, return the sum
    else:
        return sum
    
sum = recursiveSum(seperateDigits(value1))
print(sum)