
#1

#import csv

#with open('./python02/19names.csv', 'r') as cvs_file:
    #pass
    #csv_reader = csv.reader(cvs_file)

    #for line in csv_reader:
        #print(line)

#2

#import csv

#with open('./python02/19names.csv', 'r') as cvs_file:
    #csv_reader = csv.reader(cvs_file)

    #for line in csv_reader:
        #print(line)

#3
import csv

with open('./python02/19names.csv') as cvs_file:
    csv_reader = csv.DictReader(cvs_file)

    for line in csv_reader:
        print(line)