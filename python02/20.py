
#1
'''
import csv

html_output = ''
names = []

with open('python02/20story.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    print(list(csv_data))
'''

#2
'''
import csv

html_output = ''
names = []

with open('python02/20story.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    for line in csv_data:
        print(line)
'''

#3
'''
import csv

html_output = ''
names = []

with open('python02/20story.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    next(csv_data)
    next(csv_data)

    for line in csv_data:
        names.append(f"{line[0]} {line[1]}'")

for name in names:
    print(name)
'''

#4
'''
import csv

html_output = ''
names = []

with open('python02/20story.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    next(csv_data)
    next(csv_data)

    for line in csv_data:
        if line[0] == 'hi!':
            break
        names.append(f"{line[0]} {line[1]}'")

for name in names:
    print(name)
'''

#5, MY VERSION (DOSN'T WORK)

import csv

html_output = ''
names = []

with open('python02/20story.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    print('This is story one!')
    print('This one is short though but,')
    print('its very fun!')

    print(csv_data)