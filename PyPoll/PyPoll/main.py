# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

# Creating an object out of the CSV file
election_data = os.path.join('PyPoll','Resources','election_data.csv')

# defining variable type
candidate_list = []
candidate_votes = []
percent_votes = []

# Reading CSV file, data seperated by commas
with open(election_data, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)

    # loop through all data
    for row in csvreader:
# Rows 24-27 were sourced from "BKEUTHAN, guithub.""
        # If statement to count by individual candidate 
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            candidate_index = candidate_list.index(row[2])
            candidate_votes.append(1)
        else:
            candidate_index = candidate_list.index(row[2])
            candidate_votes.append(1)
            candidate_votes[candidate_index] += 1
 # Total Votes
    total_votes = len(candidate_votes)

    # Calc for percentage votes
    for n in range(len(candidate_list)):
        percentage = (candidate_votes[n]/total_votes) * 100
        percentage2 = (f" {str(round(percentage, 3))}%")
        percent_votes.append(percentage2)

    # Calc for winner
    winner = max(candidate_votes)
    winner_index = candidate_votes.index(winner)
    winning_candidate = candidate_list[winner_index]

    #Print Python Data
print("Election Results")
print("----------------")
print(f"Total Votes: {(total_votes)}")
print("----------------")
for n in range(len(candidate_list)):
    print(f"{str(candidate_list[n])}: {str(percent_votes[n])} ({str(candidate_votes[n])})")
print("----------------")
print(f"Winner: {winning_candidate}")
print("----------------")

# Exporting to .txt file
text = open("output.txt", "w")
text.write("\n")
text.write("Election Results")
text.write("\n")
text.write("----------------")
text.write("\n")
text.write(f"Total Votes: {(total_votes)}")
text.write("\n")
text.write("----------------")
text.write("\n")
for i in range(len(candidate_list)):
    text.write((f"{str(candidate_list[i])}: {str(percent_votes[i])} ({str(candidate_votes[i])}) \n"))
text.write("----------------")
text.write("\n")
text.write(f"Winner: {winning_candidate}")
text.write("\n")
text.write("----------------")