import os
import csv
import numpy as np

csvpath = os.path.join('.',"Resources",'budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    #pull out header
    csvheader = next(csvreader)
    
    
    #make variables to use in for loop
    monthly_profits = []
    net = 0
    total_months = 0    
    #because total_months becomes 1 with the first iteration
    #and the array of monthly changes has one less value than there are months, the indexes of
    #the months with greatest monthly changes in profit/loss in the for loop will be 2 more than the index of the
    #greatest monthly changes in the numpy diff_array
    gmi_month = ""
    gmd_month = ""
    
    
    #update variables the variables made for the for loop
    for row in csvreader:
        total_months += 1
        monthly_profits.append(int(row[1]))
        net += int(row[1])
        if total_months == 26:
            gmi_month = row[0]
        if total_months == 45:
            gmd_month = row[0]
    
    #make a numpy array to find the average difference in profit from month to month
    #as well as the months which had the greatest change/how much of a change there was
    monthly_array = np.array(monthly_profits)
    diff_array = np.diff(monthly_array)
    avg_change = np.average(diff_array)
    avg_change = float(round(avg_change,2))    
    greatest_increase_date = ''
    greatest_decrease_date = ""
    g_monthly_increase = max(diff_array)
    #print(g_monthly_increase)
    g_monthly_decrease = min(diff_array)
    #print(g_monthly_decrease)    
    index_gmi = np.where(diff_array == g_monthly_increase)
    #print(index_gmi)
    index_gmd= np.where(diff_array == g_monthly_decrease)
    #print(index_gmd)

#print analysis
print(["Financial Analysis"])
print(["------------------------"])
print([f"Total Months: {total_months}"])
print([f"Total: ${net}"])
print([f"Average Change: ${avg_change}"])
print([f"Greatest Increase in Profits: {gmi_month} (${g_monthly_increase})"])
print([f"Greatest Decrease in Profits: {gmd_month} (${g_monthly_decrease})"])
        
    
    
    
#making variable for output file
output_file = os.path.join(".","Analysis","pybank_analysis.txt")

#opening output file
with open(output_file, "w", newline="") as analysis:
    writer = csv.writer(analysis, delimiter=",")
    
    writer.writerow(["Financial Analysis"])
    writer.writerow(["------------------------"])
    writer.writerow([f"Total Months: {total_months}"])
    writer.writerow([f"Total: ${net}"])
    writer.writerow([f"Average Change: ${avg_change}"])
    writer.writerow([f"Greatest Increase in Profits: {gmi_month} ${g_monthly_increase}"])
    writer.writerow([f"Greatest Decrease in Profits: {gmd_month} ${g_monthly_decrease}"])
