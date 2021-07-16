import os
import csv

csvpath = os.path.join('.','election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    #pull out header
    csvheader = next(csvreader)
    #make desired variables
    total_votes = 0
    

    
    #print(csvreader) and update variables
    #for row in csvreader:

    

#print analysis
print(["Election Results"])
print(["------------------------"])
#print([f"Total Votes: {total_votes}"])
print(["------------------------"])
  
    
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
