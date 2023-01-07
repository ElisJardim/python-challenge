# Import Modules / Libraries
import os
import csv

# Create an object
election_data = os.path.join("Pypoll", "Resources", "election_data.csv")

# Create a list to capture the names of candidates
candidates = []

# Crate a list to capture the number of votes each candidate receives
num_votes = []

# Create a list to capture the percentage of total votes each candidate garners 
percent_votes = []

# Create a counter for the total number of votes 
total_votes = 0

with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    for row in csvreader:
        # Add to our vote-counter 
        total_votes += 1 
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    # Add to percent_votes list 
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percent_votes.append(percentage)
    
    # Find the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]


# Create the result string for votes per candidate (3 decimal places for percentage)
str_candidates = ""
for i in range(len(candidates)):
    str_candidates += "{candidate}: {votes:.3f}% ({total})\n".format(candidate=candidates[i], votes=percent_votes[i], total=str(num_votes[i]))

# Create the output result
result = """Election Results
-------------------------
Total Votes: {tv}
-------------------------
{candidates}-------------------------
Winner: {winner}
-------------------------
""".format(tv=total_votes, winner=winning_candidate, candidates=str_candidates)

# Display the result in the terminal
print(result)

# Save the result to a file
filename = os.path.join("PyPoll", "analysis", "result.txt")
f = open(filename, "w")
f.write(result)
f.close()
