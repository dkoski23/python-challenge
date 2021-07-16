import os
import csv

csvpath = os.path.join('.','Resources','election_data.csv')
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
    print(khan)
    print(otooley)
    print(total_votes)
    #make the percentage variables per candidate        
    per_khan = round(khan/total_votes, 5) * 100
    per_li = round(li/total_votes, 5) * 100
    per_li = round(per_li, 2)
    per_correy = round(correy/total_votes, 5) * 100   
    per_otooley = round(otooley/total_votes, 5) * 100
    
    #make dictionary of candidates and winner variable so that the winner is not hard coded
    can_dict = {"Khan": khan, "Correy": correy, "O'Tooley": otooley, "Li": li}
    
    #find the key with the highest value in can_dict, withouth hard coding
    winner = max(can_dict, key = can_dict.get)
        
    print(["Election Results"])
    print(["------------------------"])
    print([f"Total Votes: {total_votes}"])
    print(["------------------------"])
    print([f"Khan: {per_khan}% ({khan})"])
    print([f"Li: {per_li}% ({li})"])
    print([f"Correy: {per_correy}% ({correy})"])
    print([f"O'Tooley: {per_otooley}% ({otooley})"])
    print(["------------------------"])
    print([f"Winner: {winner}"])
    print(["------------------------"])
    
#making variable for output file
output_file = os.path.join(".","Analysis","pypoll_analysis.txt")

#opening output file
with open(output_file, "w", newline="") as analysis:
    writer = csv.writer(analysis, delimiter=",")
    
    writer.writerow(["Election Results"])
    writer.writerow(["------------------------"])
    writer.writerow([f"Total Votes: {total_votes}"])
    writer.writerow(["------------------------"])
    writer.writerow([f"Khan: {per_khan}% ({khan})"])
    writer.writerow([f"Li: {per_li}% ({li})"])
    writer.writerow([f"Correy: {per_correy}% ({correy})"])
    writer.writerow([f"O'Tooley: {per_otooley}% ({otooley})"])
    writer.writerow(["------------------------"])
    writer.writerow([f"Winner: {winner}"])
    writer.writerow(["------------------------"])
