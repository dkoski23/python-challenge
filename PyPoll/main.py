import os
import csv

csvpath = os.path.join('.','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    #pull out header
    csvheader = next(csvreader)
    #make desired variables
    total_votes = 0
    candidates = []
    khan = 0
    li = 0
    otooley = 0
    correy = 0

    
    #print(csvreader) and update variables
    #print(csvreader)
    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
    print(total_votes)
    print(candidates)
    

#print analysis
#print(["Election Results"])
#print(["------------------------"])
#print([f"Total Votes: {total_votes}"])
#print(["------------------------"])
#print([f"Total: ${net}"])
#print([f"Average Change: ${avg_change}"])
#print([f"Greatest Increase in Profits: {greatest_increase_date} ${greatest_increase_num}"])
#print([f"Greatest Decrease in Profits: {greatest_decrease_date} ${greatest_decrease_num}"])
        
    
    
    
#making variable for output file
#output_file = os.path.join(".","pypoll_analysis.txt")

#opening output file
#with open(output_file, "w", newline="") as analysis:
    #writer = csv.writer(analysis, delimiter=",")
    
    #writer.writerow(["Election Results"])
    #writer.writerow(["------------------------"])
    #writer.writerow([f"Total Votes: {total_votes}"])
    #writer.writerow(["------------------------"])
    #writer.writerow([f""])
    #writer.writerow([f""])
    #writer.writerow([f""])
    #writer.writerow([f""])
