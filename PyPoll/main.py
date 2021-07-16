import os
import csv

csvpath = os.path.join('.','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    #pull out header
    csvheader = next(csvreader)
    #make variables for total votes, list of candidates, candidate totals
    total_votes = 0
    candidates = []
    khan = 0
    li = 0
    otooley = 0
    correy = 0

    
    #update variables by running through the lines of the csv file
    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2] == "Khan":
            khan += 1
        if row[2] == "Li":
            li += 1
        if row[2] == "Correy":
            correy += 1
        if row[2] == "O'Tooley":
            otooley += 1
            
    per_khan = round(khan/total_votes, 5) * 100
    print(per_khan)
    per_li = round(li/total_votes, 5) * 100
    print(per_li)
    per_correy = round(correy/total_votes, 5) * 100
    print(per_correy)
    per_otooley = round(otooley/total_votes, 5) * 100
    print(per_otooley)
        
        
    print(["Election Results"])
    print(["------------------------"])
    print([f"Total Votes: {total_votes}"])
    print(["------------------------"])
    print([f"Khan: ({khan})"])
    print([f"Li: ({li})"])
    print([f"Correy: ({correy})"])
    print([f"O'Tooley: ({otooley})"])

    

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
