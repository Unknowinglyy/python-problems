#this program will take in two comma separated string of equal length and determine if one is a scrambled version of the other. Will print Yes if it is, No if it is not.

import sys

value1 = sys.argv[1]
scrambled = False

#seperate the strings
string1 = value1.split(",")[0]
string2 = value1.split(",")[1]

#double checking the strings are the same length, if not, then no need to check further
if len(string1) != len(string2):
    print("No")
    sys.exit()

dict1 = {}
dict2 = {}

#since strings are of equal length, can populate both dictionaries within the same loop
for i in range(len(string1)):
    if string1[i] in dict1:
        dict1[string1[i]] += 1
    elif string1[i] not in dict1:
        dict1[string1[i]] = 1
    
    if string2[i] in dict2:
        dict2[string2[i]] += 1
    elif string2[i] not in dict2:
        dict2[string2[i]] = 1

#check between the two dictionaries to see if they are the same
for char in dict1:
    if char in dict2:
        if dict1[char] == dict2[char]:
            scrambled = True
        else:
            scrambled = False
            break
    else:
        scrambled = False
        break

#output the result
if scrambled:
    print("Yes")
else:
    print("No")