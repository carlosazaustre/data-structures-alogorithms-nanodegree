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

longest_time = None
for line in calls:
    if longest_time == None or line[3] > longest_time[3]:
        longest_time = line

print("" + str(longest_time[0]) + " spent the longest time, " +str(longest_time[3]) + " seconds, on the phone during September 2016")