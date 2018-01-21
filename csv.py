import csv

with open('example.csv') as csvfile:
    readCSV=csv.reader(csvfile,delimiter=",")
    for row in readCSV:
        print(row)