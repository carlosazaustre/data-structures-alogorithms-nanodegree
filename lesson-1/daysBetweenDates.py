def isLeapYear(year):
  if year % 400 == 0
    return True
  if year % 100 == 0
    return False
  if year % 4 == 0
    return True
  return False

def daysInMonth(year, month):
  months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  if isLeapYear(year):
    months[1] = 29
  return months[month - 1]

def nextDay(year, month, day):
  """Simple version: assume every month has 30 days"""
  if day < daysInMonth(year, month):
    return year, month, day + 1
  else:
    if month == 12:
      return year + 1, 1, 1
    else:
      return year, month + 1, 1
        
def dateIsBefore(year1, month1, day1, year2, month2, day2):
  """
  Returns True if year1-month1-day1 is before 
  year2-month2-day2. Otherwise return False
  """
  if year1 < year2:
    return True
  if year1 == year2:
    if month1 < month2:
      return True
    if month1 == month2:
      return day1 < day2
  return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
  """
  Calculates the number of days between two dates.
  """
  assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
  
  days = 0
  while dateIsBefore(year1, month1, day1, year2, month2, day2):
    year1, month1, day1 = nextDay(year1, month1, day1)
    days += 1
  
  return days


def testDaysBetweenDates():
  # test same day
  assert(daysBetweenDates(2017, 12, 30, 2017, 12, 30) == 0)
  # test adjacent days
  assert(daysBetweenDates(2017, 12, 30, 2017, 12, 31) == 1)
  # test new year
  assert(daysBetweenDates(2017, 12, 30, 2018, 1,  1)  == 2)
  # test full year difference
  assert(daysBetweenDates(2012, 6, 29, 2013, 6, 29)  == 365)
  
  print("Congratulations! Your daysBetweenDates")
  print("function is working correctly!")
    
testDaysBetweenDates()
