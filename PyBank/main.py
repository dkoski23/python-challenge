import os
import csv

csvpath = os.path.join('.','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    #pull out header
    csvheader = next(csvreader)
    #make desired variables
    net = 0
    total_months = 0
    avg_change = 0
    greatest_increase_num = 0
    greatest_increase_date = ''
    greatest_decrease_num = 0
    greatest_decrease_date = ""
    
    #print(csvreader) and update variables
    for row in csvreader:
        total_months +=1
        net += int(row[1])
        if int(row[1]) > greatest_increase_num:
            greatest_increase_num = int(row[1])
            greatest_increase_date = row[0]
        if int(row[1]) < greatest_decrease_num:
            greatest_decrease_num = int(row[1])
            greatest_decrease_date = row[0]
    
    avg_change = net/total_months
    avg_change = round(avg_change,2)
    #print(avg_change)        
    #print(greatest_decrease_date)
    #print(greatest_increase_date)   
    #print(greatest_increase_num)    
    #print(net)
    #print(total_months)

#making variable for output file
output_file = os.path.join(".","pybank_analysis.txt")

#opening output file
with open(output_file, "w", newline="") as analysis:
    writer = csv.writer(analysis, delimiter=",")
    
    writer.writerow(["Financial Analysis"])
    writer.writerow(["------------------------"])
    writer.writerow([f"Total Months: {total_months}"])
    
    
