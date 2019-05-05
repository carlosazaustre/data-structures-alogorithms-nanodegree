"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

calls_time = []
calls_numbers = []

for call in calls:
    if call[0] not in calls_numbers:
        calls_numbers.append(call[0])
        calls_time.append(int(call[3]))
    else:
        index = calls_numbers.index(call[0])
        calls_time[index] += int(call[3])

    if call[1] not in calls_numbers:
        calls_numbers.append(call[0])
        calls_time.append(int(call[3]))
    else:
        index = calls_numbers.index(call[1])
        calls_time[index] += int(call[3])

max_time = 0
for time in calls_time:
    if time > max_time:
        max_time = time

index = calls_time.index(max_time)

print(str(calls_numbers[index]) + " spent the longest time, " + str(calls_time[index]) + " seconds, on the phone during September 2016")