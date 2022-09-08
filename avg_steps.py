import csv
import calendar

monthAvg = {}
with open('steps.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter = ',')
    count = 0
    for record in reader:
        if count == 0:
            count += 1
        else:
            month = calendar.month_name[int(record[0])]
            if int(record[0]) not in monthAvg.keys():
                monthAvg[int(record[0])] = [int(record[1])]
            else:
                monthAvg[int(record[0])].append(int(record[1]))
csvfile.close()

with open('avg_steps.csv', 'w') as avg_steps:
    avg_steps_writer = csv.writer(avg_steps, delimiter = ',')
    months = list(monthAvg.keys())
    writer = csv.DictWriter(avg_steps, fieldnames = ['Month', ' Average Steps'])
    writer.writeheader()
    for month in months:
        avg_steps_writer.writerow([calendar.month_name[month],round(sum(monthAvg[month])/len(monthAvg[month]),2)])
avg_steps.close()
