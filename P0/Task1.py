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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def countUniqueNumbers(texts, calls):
    unique_numbers = set([])
    for line in texts:
        unique_numbers.add(line[0])
        unique_numbers.add(line[1])
    for line in calls:
        unique_numbers.add(line[0])
        unique_numbers.add(line[1])
    return len(unique_numbers)

print("There are "+ str(countUniqueNumbers(texts, calls)) +" different telephone numbers in the records.")