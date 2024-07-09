#This program takes a roman numeral as an argument and converts it to a number.
import sys

value1 = sys.argv[1]

romeDict = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
curr = 0
prev = 0
total = 0
for roman in value1:
    #find the equivalent number of the roman numeral
    curr = romeDict[roman]
    #get the current total
    total += curr
    #if the current number is greater than the previous number, subtract the previous number twice from the total
    if curr > prev:
        total -= 2*prev
    #set the previous number to the current number
    prev = curr

print(total)