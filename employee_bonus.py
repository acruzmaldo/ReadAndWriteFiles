import csv

infile = open('employeepay.csv', 'r')
csvfile = csv.reader(infile, delimiter = ',')

print('ID, EmpFname, EmpLname, Salary, Bonus') # this will skip the first row
next(csvfile)

for record in csvfile:
    base_salary = int(record[3])
    bonus = base_salary * float(record[4])
    total_comp = bonus + base_salary

    print('ID: ', record[0])
    print('First Name: ', record[1])
    print('Last Name: ', record[2])
    print('Total Comp: ', "${:,.2f}".format(total_comp), '\n')

