
import csv

infile = open('customers.csv', 'r')
csvfile = csv.reader(infile, delimiter = ',')

outfile = open('customer_country.csv', 'w')

outfile.write('Full Name, Country' + '\n')

next(csvfile) # this will skip the first row

count = 0
for record in csvfile:
    name = record[1] + ' ' + record[2]
    country = ' ' + record[4]
    count += 1
    outfile.write(name + ',' + country + '\n')
 
print('Total Customers: ', count)

outfile.close()