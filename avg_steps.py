import csv

infile = open('steps.csv', 'r')

csvfile = csv.reader(infile, delimiter = ',')
outfile = open('avg_steps.csv', 'w')

sum1 = sum2 = sum3 = sum4 = sum5 = sum6 = sum7 = sum8 = sum9 = sum10 = sum11 = sum12 = 0
count1 = count2 = count3 = count4 = count5 = count6 = count7 = count8 = count9 = count10 = count11 = count12 = 0

writer = csv.DictWriter(outfile, fieldnames = ['Month', ' Average Steps'])
writer.writeheader()

for record in csvfile:

    if record[0] == str(1):
        sum1 += int(record[1])
        count1 += 1
        average1= sum1/count1

    elif record[0] == str(2):
        sum2 += int(record[1])
        count2 += 1
        average2= sum2/count2
    
    elif record[0] == str(3):
        sum3 += int(record[1])
        count3 += 1
        average3 = sum3/count3

    elif record[0] == str(4):
        sum4 += int(record[1])
        count4 += 1
        average4= sum4/count4
    
    elif record[0] == str(5):
        sum5 += int(record[1])
        count5 += 1
        average5= sum5/count5

    elif record[0] == str(6):
        sum6 += int(record[1])
        count6 += 1
        average6= sum6/count6

    elif record[0] == str(7):
        sum7 += int(record[1])
        count7 += 1
        average7= sum7/count7

    elif record[0] == str(8):
        sum8 += int(record[1])
        count8 += 1
        average8= sum8/count8

    elif record[0] == str(9):
        sum9 += int(record[1])
        count9 += 1
        average9= sum9/count9

    elif record[0] == str(10):
        sum10 += int(record[1])
        count10 += 1
        average10= sum10/count10

    elif record[0] == str(11):
        sum11 += int(record[1])
        count11 += 1
        average11= sum11/count11
    
    elif record[0] == str(12):
        sum12 += int(record[1])
        count12 += 1
        average12= sum12/count12

outfile.write('January')
outfile.write(', ')
outfile.write(str(round(average1,2)))
outfile.write('\n')

outfile.write('February')
outfile.write(', ')
outfile.write(str(round(average2,2)))
outfile.write('\n')

outfile.write('March')
outfile.write(', ')
outfile.write(str(round(average3,2)))
outfile.write('\n')

outfile.write('April')
outfile.write(', ')
outfile.write(str(round(average4,2)))
outfile.write('\n')

outfile.write('May')
outfile.write(', ')
outfile.write(str(round(average5,2)))
outfile.write('\n')

outfile.write('June')
outfile.write(', ')
outfile.write(str(round(average6,2)))
outfile.write('\n')

outfile.write('July')
outfile.write(', ')
outfile.write(str(round(average7,2)))
outfile.write('\n')

outfile.write('August')
outfile.write(', ')
outfile.write(str(round(average8,2)))
outfile.write('\n')

outfile.write('September')
outfile.write(', ')
outfile.write(str(round(average9,2)))
outfile.write('\n')

outfile.write('October')
outfile.write(', ')
outfile.write(str(round(average10,2)))
outfile.write('\n')

outfile.write('November')
outfile.write(', ')
outfile.write(str(round(average11,2)))
outfile.write('\n')

outfile.write('December')
outfile.write(', ')
outfile.write(str(round(average12,2)))
outfile.write('\n')
