import csv
import pprint

#converting CSV data to TXT data

month = 10
day = 1

while month < 13:
    day2 = day
    if day < 10:
        day2 = str(0)+str(day)
    fname = 'RUMOI/NPHAS_RUM-2021{0}{1}00.csv'.format(month,day2)
    fname2 = 'Y3{0}{1}.txt'.format(month,day2)
    with open(fname) as f:
        reader = csv.reader(f)
        for row in reader:
            Y1 = str(row[2])
            Y2 = str(row[3])
            f = open(fname2, 'a')
            f.write(Y1)
            f.write(' ')
            f.write(Y2) 
            f.write('\n')
    day += 1
    if day > 31:
        month += 1
        day = 1
    if month ==11 and day >30:
        month += 1
        day = 1







    

    




        