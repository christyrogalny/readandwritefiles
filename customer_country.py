import csv

infile = open('customers.csv', 'r')
csvfile = csv.reader(infile, delimiter = ',')
outfile = open('customer_country.csv', 'w')

next(csvfile) #this will skip the first row

writer = csv.DictWriter(outfile, fieldnames = ['Full Name', ' Country'])
writer.writeheader()

for record in csvfile:
    outfile.write(record[1])
    outfile.write(' ')
    outfile.write(record[2])
    outfile.write(', ')
    outfile.write(record[4])
    outfile.write('\n')

outfile.close()
