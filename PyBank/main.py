import os
import csv
import numpy as np

csvpath = os.path.join('.','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    #pull out header
    csvheader = next(csvreader)
    #make desired variables
    net = 0
    total_months = 0
    monthly_profits = []
    
    #print(csvreader) and update variables
    for row in csvreader:
        monthly_profits.append(int(row[1]))
        total_months +=1
        net += int(row[1])
    #for item in diff_array:
        #if item > g_monthly_increase:
            #greatest_increase_date = row[0]
        #if int(row[1]) < greatest_decrease_num:
            #greatest_decrease_date = row[0]
    
    #make a numpy array to find the average difference in profit from month to month
    monthly_array = np.array(monthly_profits)
    #print(monthly_array)
    diff_array = np.diff(monthly_array)
    #print(diff_array)
    avg_change = np.average(diff_array)
    avg_change = float(round(avg_diff,2))
    
    greatest_increase_date = ''
    greatest_decrease_date = ""
    g_monthly_increase = max(diff_array)
    print(g_monthly_increase)
    g_monthly_decrease = min(diff_array)
    print(g_monthly_decrease)
    test = np.where(diff_array == g_monthly_increase)
    print(test)
    
    
#print analysis
print(["Financial Analysis"])
print(["------------------------"])
print([f"Total Months: {total_months}"])
print([f"Total: ${net}"])
print([f"Average Change: ${avg_change}"])
print([f"Greatest Increase in Profits: {greatest_increase_date} $"])
print([f"Greatest Decrease in Profits: {greatest_decrease_date} $"])
        
    
    
    
#making variable for output file
output_file = os.path.join(".","pybank_analysis.txt")

#opening output file
with open(output_file, "w", newline="") as analysis:
    writer = csv.writer(analysis, delimiter=",")
    
    writer.writerow(["Financial Analysis"])
    writer.writerow(["------------------------"])
    writer.writerow([f"Total Months: {total_months}"])
    writer.writerow([f"Total: ${net}"])
    #writer.writerow([f"Average Change: ${avg_change}"])
    #writer.writerow([f"Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase_num}"])
    #writer.writerow([f"Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease_num}"])
    
