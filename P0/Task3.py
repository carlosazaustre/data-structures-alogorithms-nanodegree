"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def isBangaloreNumber(telephone_number):
  if telephone_number[0:5] == "(080)":
    return True

def getAreaCode(telephone_number):
  if telephone_number[0] == "(":
    # it's a fixed line
    count = 0
    for number in telephone_number:
      if number != ")":
        count += 1
      else:
        break
    return telephone_number[1:count]


  elif telephone_number[0] == "7" or telephone_number[0] == "8" or telephone_number[0] == "9":
    # it's a mobile number
    return telephone_number[0:4]

  elif telephone_number[0:3] == "140":
    # it's a telemarketer
    return telephone_number[0:3]

def findAllAreaCodes(calls):
  codes = []
  for line in calls:
    # Check if the calling one is from Bangalore
    if isBangaloreNumber(line[0]):
      # Get the area code from the receiving one
      code = getAreaCode(line[1])
      if code not in codes:
        codes.append(code)
  return sorted(codes)

def printListOfCodes(codes):
  print("The numbers called by people in Bangalore have codes:")
  for code in codes:
    print(code)

def numberOfCallsFromAndToBangalore(calls):
  matching_calls = 0
  from_bangalore_calls = 0
  for line in calls:
    if isBangaloreNumber(line[0]):
      from_bangalore_calls += 1
      if isBangaloreNumber(line[1]):
        matching_calls += 1
  return matching_calls, from_bangalore_calls

def printPercentageBangaloreCalls(number, total):
  percentage = (float(number) / float(total)) * 100
  percentage = round(percentage, 2)
  print(str(percentage) + " percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")


# Part A
codes = findAllAreaCodes(calls)
printListOfCodes(codes)

# Part B
number, total = numberOfCallsFromAndToBangalore(calls)
printPercentageBangaloreCalls(number, total)