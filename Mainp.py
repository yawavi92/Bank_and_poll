#dependencies
import os
import csv

#file  to output
file_to_load = "raw_data/election_data.csv"
file_to_output = "analysis/election_results.txt"

#set a path
budget_data = os.path.join("PyPoll/Resources/election_data.csv")

#store variable

# voter option 
candidate_opt= []
#list of candidate
candidate_list= []
# total vote for each candidate
candidate_vote = []

#percentage vote for each candidate


vote_percent =[]

#total vote for all candidate
vote = []

#Read the file
with open(budget_data, "r") as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter= "," )
   
    
# #The total number of votes cast
    for row in csv_reader: 
        vote.append(row["Voter ID"])
        total_vote = len(vote)
    
#A complete list of candidates who received votes
        #candidate_opt.append(row["Candidate"])
        #runners = set(candidate_opt)
       
#The total number of votes each candidate won
        if row["Candidate"] not in candidate_list:
            candidate_list.append(row["Candidate"])
            index = candidate_list.index(row["Candidate"])
            candidate_vote.append(1)
        else:
            index = candidate_list.index(row["Candidate"])
            candidate_vote[index] += 1

#The percentage of votes each candidate won   
    for item in candidate_vote:
        per_candidate = (item/total_vote)*100
        vote_percent.append(per_candidate)
    print(vote_percent)
#The winner of the election based on popular vote
    winner = max(candidate_vote)
    index = candidate_vote.index(winner)
    winning_candidate = candidate_list[index]
   

  
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_vote)}")
print("--------------------------")
for i in range(len(candidate_list)):
    print(f"{candidate_list[i]}: {str(vote_percent[i])} ({str(candidate_vote[i])})")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

# Exporting to .txt file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(total_vote)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidate_list)):
    line = str(f"{candidate_list[i]}: {str(vote_percent[i])} ({str(total_vote[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
    
