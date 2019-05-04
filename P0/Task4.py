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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def getListOfNumbers(number_making_call, number_receiving_call, registry_list):
    list_of_numbers = []
    position = None

    if number_making_call:
        position = 0
    if number_receiving_call:
        position = 1

    for number in registry_list:
        if number[position] not in list_of_numbers:
            list_of_numbers.append(number[position])
    
    return list_of_numbers

def getPossibleTelemarketers(list_of_calls, list_of_texts):
    list_of_possible_telemarketers = []

    list_of_numbers_making_calls = sorted(getListOfNumbers(True, False, list_of_calls))
    list_of_numbers_receiving_calls = sorted(getListOfNumbers(False, True, list_of_calls))
    list_of_numbers_sending_texts = sorted(getListOfNumbers(True, False, list_of_texts))
    list_of_numbers_receiving_texts = sorted(getListOfNumbers(False, True, list_of_texts))

    for number in list_of_numbers_making_calls:
        if number not in list_of_numbers_receiving_calls:
            if number not in list_of_numbers_sending_texts:
                if number not in list_of_numbers_receiving_texts:
                    list_of_possible_telemarketers.append(number)

    return list_of_possible_telemarketers

def printPossibleTelemarketers(list_of_numbers):
    print("These numbers could be telemarketers: ")
    for number in list_of_numbers:
        print(number)

list_of_possible_telemarketers = getPossibleTelemarketers(calls, texts)
printPossibleTelemarketers(list_of_possible_telemarketers)
