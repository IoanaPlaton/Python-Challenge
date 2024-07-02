#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[114]:


#PyPoll Instructions

#In this Challenge, you are tasked with helping a small, rural town modernize its vote-counting process.
#You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: “Voter ID”, “County”, and “Candidate”. Your task is to create a Python script that analyzes the votes and calculates each of the following values:

#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote

import os
import csv

election_data = os.path.join ('.' , 'Resources' , 'election_data.csv')

#Candidate Options and Vote Counters 
candidates = []
vote_count = []
percent_votes = []

# Total vote counter
total_votes = 0

#Winning Candidate and Winning County Tracker

#open and read csv 
with open (election_data, newline = "") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #print(csv_reader)

# Read the header row first 
    csv_header = next(csv_reader)
    #print(csv_header)

#Add candidates and their votes to the list. If candidte is on the list only add to their vote count.    
    for row in csv_reader:
        total_votes += 1
        
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            vote_count.append(1)
        else:
            index = candidates.index(row[2])
            vote_count[index] += 1
            
#The total number of votes cast
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(total_votes)}")
print("--------------------------")

#A complete list of candidates who received votes & #The total number of votes each candidate won      
#The percentage of votes each candidate won

for votes in vote_count:
    percentage = (votes/total_votes) * 100
    percentage = round(percentage)
    percentage = "%.0f%%" % percentage
    percent_votes.append(percentage)

for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(vote_count[i])})")

#The winner of the election based on popular vote
winner = max(vote_count)
index = vote_count.index(winner)
winning_candidate = candidates[index]

print("--------------------------")

print(f"Winner: {winning_candidate}")

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.

output_path = os.path.join('.', 'Analysis', 'PollAnalysis.txt')   
with open(output_path, "w") as txtfile:
    txtfile.write("Election Results" + "\n")

    txtfile.write("--------------------------" + "\n")

    txtfile.write(f"Total Votes: {str(total_votes)}" + "\n")

    txtfile.write("--------------------------" + "\n")
    
    for i in range(len(candidates)):
        line = str(f"{candidates[i]}: {str(percent_votes[i])} ({str(vote_count[i])})")
        txtfile.write('{}\n'.format(line))
    
    txtfile.write("--------------------------" + "\n")

    txtfile.write(f"Winner: {winning_candidate}" + "\n")




# In[ ]:




