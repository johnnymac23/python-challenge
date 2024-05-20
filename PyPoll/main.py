import os
import csv


csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    csv_header = next(csvreader)

    total_votes = 0
    candidate_votes = {}


    for row in csvreader:
        total_votes = total_votes + 1
        candidate = row[2]

        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1


    winner = max(candidate_votes, key=candidate_votes.get)

print("Results")
print(f"Total Votes: {total_votes}")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage}% ({votes})")
print(f"Winner: {winner}")

