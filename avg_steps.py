
import csv

infile = open('steps.csv', 'r')
csvfile = csv.reader(infile, delimiter = ',')

outfile = open('avg_steps.csv', 'w')

outfile.write('Month, Average Steps' + '\n')

next(csvfile) # this will skip the first row

count = 0
monthly_steps = 0
for record in csvfile:
    
    # January
    if record[0] == '1':
        month = 'January'
        monthly_steps += int(record[1])
        count += 1
        if count == 31:
            avg_steps = monthly_steps/count
            outfile.write(month + ', ' + "{:.7}".format(str(avg_steps)) + '\n')
            count = 0
            monthly_steps = 0

    # Fenruary
    elif record[0] == '2':    
        month = 'February'
        monthly_steps += int(record[1])
        count += 1
        if count == 28:
            avg_steps = monthly_steps/count
            outfile.write(month + ', ' + "{:.7}".format(str(avg_steps)) + '\n')
            count = 0
            monthly_steps = 0

    # March
    elif record[0] == '3':    
        month = 'March'
        monthly_steps += int(record[1])
        count += 1
        if count == 31:
            avg_steps = monthly_steps/count
            outfile.write(month + ', ' + "{:.7}".format(str(avg_steps)) + '\n')
            count = 0
            monthly_steps = 0

    # April
    elif record[0] == '4':    
        month = 'April'
        monthly_steps += int(record[1])
        count += 1
        if count == 30:
            avg_steps = monthly_steps/count
            outfile.write(month + ', ' + "{:.7}".format(str(avg_steps)) + '\n')
            count = 0
            monthly_steps = 0

    # May
    elif record[0] == '5':    
        month = 'May'
        monthly_steps += int(record[1])
        count += 1
        if count == 31:
            avg_steps = monthly_steps/count
            outfile.write(month + ', ' + "{:.7}".format(str(avg_steps)) + '\n')
            count = 0
            monthly_steps = 0


    # June
    elif record[0] == '6':    
        month = 'June'
        monthly_steps += int(record[1])
        count += 1
        if count == 30:
            avg_steps = monthly_steps/count
            outfile.write(month + ', ' + "{:.7}".format(str(avg_steps)) + '\n')
            count = 0
            monthly_steps = 0


    # July
    elif record[0] == '7':    
        month = 'April'
        monthly_steps += int(record[1])
        count += 1
        if count == 31:
            avg_steps = monthly_steps/31
            outfile.write(month + ', ' + "{:.7}".format(str(avg_steps)) + '\n')
            count = 0
            monthly_steps = 0


    # August
    elif record[0] == '8':    
        month = 'April'
        monthly_steps += int(record[1])
        count += 1
        if count == 31:
            avg_steps = monthly_steps/count
            outfile.write(month + ', ' + "{:.7}".format(str(avg_steps)) + '\n')
            count = 0
            monthly_steps = 0


    # September
    elif record[0] == '9':    
        month = 'September'
        monthly_steps += int(record[1])
        count += 1
        if count == 30:
            avg_steps = monthly_steps/count
            outfile.write(month + ', ' + "{:.7}".format(str(avg_steps)) + '\n')
            count = 0
            monthly_steps = 0


    # October
    elif record[0] == '10':    
        month = 'October'
        monthly_steps += int(record[1])
        count += 1
        if count == 31:
            avg_steps = monthly_steps/count
            outfile.write(month + ', ' + "{:.7}".format(str(avg_steps)) + '\n')
            count = 0
            monthly_steps = 0


    # November
    elif record[0] == '11':    
        month = 'November'
        monthly_steps += int(record[1])
        count += 1
        if count == 30:
            avg_steps = monthly_steps/count
            outfile.write(month + ', ' + "{:.7}".format(str(avg_steps)) + '\n')
            count = 0
            monthly_steps = 0


    # December
    elif record[0] == '12':    
        month = 'December'
        monthly_steps += int(record[1])
        count += 1
        if count == 31:
            avg_steps = monthly_steps/count
            outfile.write(month + ', ' + "{:.7}".format(str(avg_steps)) + '\n')
            count = 0
            monthly_steps = 0

outfile.close()