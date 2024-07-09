#this program finds the total amount of days between two dates. The dates are inputted as a comma separated string in the format of yyyy-mm-dd. The first date is considerd the end date and the second date is considered the start date. If the start date is in the future, then the total amount of days will be negative.
import sys

value1 = sys.argv[1]

#seperate the dates
date1 = value1.split(",")[0]
date2 = value1.split(",")[1]

year1 = date1.split("-")[0]
month1 = date1.split("-")[1]
day1 = date1.split("-")[2]

year2 = date2.split("-")[0]
month2 = date2.split("-")[1]
day2 = date2.split("-")[2]

yearDiff = int(year1) - int(year2)
monthDiff = int(month1) - int(month2)
dayDiff = int(day1) - int(day2)

totalDays = 0
totalDays += yearDiff * 365
totalDays += monthDiff * 30
totalDays += dayDiff

print(totalDays)