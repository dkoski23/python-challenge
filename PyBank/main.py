import os
import csv
import numpy as np

csvpath = os.path.join('.','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    #pull out header
    csvheader = next(csvreader)
    
    #make a numpy array to find the average difference in profit from month to month
    monthly_array = np.array(monthly_profits)
    #print(len(monthly_array))
    diff_array = np.diff(monthly_array)
    #print(len(diff_array))
    avg_change = np.average(diff_array)
    avg_change = float(round(avg_diff,2))    
    greatest_increase_date = ''
    greatest_decrease_date = ""
    g_monthly_increase = max(diff_array)
    print(g_monthly_increase)
    g_monthly_decrease = min(diff_array)
    print(g_monthly_decrease)
    #because of total_months in the below for loop starting becoming 1 with the first value
    #and the array of monthly changes having one less value than there are months, the indexes of
    #the months with greatest monthly changes in profit/loss will be off by 2 from the index of the
    #greatest monthly changes in the numpy diff_array
    index_gmi = np.where(diff_array == g_monthly_increase)
    print(index_gmi)
    
    
    
    
    
    #make desired variables
    net = 0
    total_months = 0
    monthly_profits = []
    
    #print(csvreader) and update variables
    for row in csvreader:
        monthly_profits.append(int(row[1]))
        total_months +=1
        net += int(row[1])
        if total_months == 26:
            print(row[0])
    
    
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
    
