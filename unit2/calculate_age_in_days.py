# calculate days passed from the day you were born until today's date
# including lap years
# Input: birthday and current date
# Output: number of days between those 2 dates


# 1. days left in the birthday month
# 2. months until the current month
# 3. days left in the current month

def nextDay(year, month, day):
  if (day == 30 and month == 12):
    return (year+1, 1, 1)
  elif (day == 30):
    return (year, month+1, 1)
  else:
    return (year, month, day+1)


# test nextDay
print nextDay(2012,6,29)
print nextDay(2012,1,30)
print nextDay(2013,5,30)

