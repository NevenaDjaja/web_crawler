# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct ouptuts yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

# if (year is not divisible by 4) then (it is a common year)
# else
# if (year is not divisible by 100) then (it is a leap year)
# else
# if (year is not divisible by 400) then (it is a common year)
# else (it is a leap year)

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# return if year is a leap year
def isLeapYear(year):
  if (year%4 != 0):
    return False
  else:
    if (year%100 != 0):
      return True
    elif (year%400 != 0):
      return False
    else:
      return True

# return number of days in a given month
def daysInMonth(year,month):
  if isLeapYear(year):
    days_in_month[1] = 29
  return days_in_month[month-1]

# return the next date given a current date
def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year,month):
        return year, month, day + 1
    # the last day of the month
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
        
# return number of days between year2, month2, day2 and year1, month1, day1
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
        
    days = 0
    while (numberOfDays(year1, month1, day1) < numberOfDays(year2, month2, day2)):
      (year1, month1, day1) = nextDay(year1, month1, day1)
      days += 1
    return days

def numberOfDays(year, month, day):
  return year*360 + month*30 + day


def daysInMonth_test():
  if daysInMonth(2001,1) == 31 and daysInMonth(1997,4) == 30:
    print("Test passed")
  else:
    print("Test failed")

daysInMonth_test()

def isLeapYear_test():
  if isLeapYear(2004) is True:
    print("Leap year test passed!")
  else: 
    print("Leap year test failed!")

isLeapYear_test()
print("DAYS BETWEEN MY BIRTHDAY AND TODAY")
print(daysBetweenDates(1983, 3, 13, 2014, 8, 10))

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")

test()
    
