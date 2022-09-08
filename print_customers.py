#this prints out name from csv file one at the time -- press enter to go to next name
import csv

infile = open('customers.csv', 'r')

csvfile = csv.reader(infile, delimiter = ',')

next(csvfile)   #this will skip the first row (aka header)

for record in csvfile:
    print('ID:',record[0])
    print('Fname:',record[1])
    print('Lname:',record[2])
    print('City:',record[3])
    print('Country:',record[4])
    print('Phone:',record[5])

    input()

