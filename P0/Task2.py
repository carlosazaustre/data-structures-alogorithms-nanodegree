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

def saveCall(phone, time, phone_list, time_list):
    if phone not in phone_list:
        phone_list.append(phone)
        time_list.append(int(time))
    else:
        index = phone_list.index(phone)
        time_list[index] += int(time)

def getMaxTime(time_list):
    max_time = 0
    for time in calls_time:
    if time > max_time:
        max_time = time
    return max_time

calls_time = []
calls_numbers = []

for call in calls:
    saveCall(call[0], call[3], calls_number, calls_time)
    saveCall(call[1], call[3], calls_number, calls_time)

max_time = getMaxTime(calls_time)
index = calls_time.index(max_time)

print(str(calls_numbers[index]) + " spent the longest time, " + str(calls_time[index]) + " seconds, on the phone during September 2016")