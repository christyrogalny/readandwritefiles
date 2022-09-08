import csv

infile = open('employeepay.csv', 'r')
csvfile = csv.reader(infile, delimiter = ',')

next(csvfile) 

for record in csvfile:
    print('ID:',record[0])
    print('Fname:',record[1])
    print('Lname:',record[2])
    print('Salary:',record[3])
    print('Bonus:',record[4])

    input()
