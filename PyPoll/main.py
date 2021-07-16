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
            
    #make the percentage variables per candidate        
    per_khan = round(khan/total_votes, 5) * 100
    per_li = (li/total_votes) * 100
    per_li = round(per_li, 2)
    per_correy = round(correy/total_votes, 5) * 100   
    per_otooley = round(otooley/total_votes, 5) * 100
        
        
    print(["Election Results"])
    print(["------------------------"])
    print([f"Total Votes: {total_votes}"])
    print(["------------------------"])
    print([f"Khan: {per_khan}% ({khan})"])
    print([f"Li: {per_li}% ({li})"])
    print([f"Correy: {per_correy}% ({correy})"])
    print([f"O'Tooley: {per_otooley}% ({otooley})"])
    print(["------------------------"])
    print([f"Winner: ])
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
