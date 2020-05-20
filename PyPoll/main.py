# -*- coding: utf-8 -*-
"""
Created on Thu May 14 22:36:46 2020

@author: gleix
"""

# OS Module to allow us to create paths across operating systems.
import os

# Module for reading CSV files
import csv

csvpath = os.path.join("..","PyPoll","Resources","Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")

CanidateName = []
CanidateVoteCnt = []
TotalVotes = 0
CanidateCnt = 0
CanidatePcnt = 0.0
CanidateFound = False
MaxPcnt = 0.0
WinnerSpot = 0


# Open the CSV File

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#   print(csvreader)    
#   Pull in header from the file
    csv_header = next(csvreader)
  
# Read Through Each Record
    for row in csvreader: 
 
# Keep Track of Total Votes
        TotalVotes = TotalVotes + 1
        CanidateFound = False
    
 # Calculate Canidate Totals       
        if CanidateCnt == 0:
            CanidateCnt = 1
            CanidateName.append(row[2])
            CanidateVoteCnt.append(1)
           
        else:
            # Check to see if new canidate (For Loop) are in my lists
            # If Canidate Exists, Add one to Vote Counter.
            for x in range(CanidateCnt):
                if row[2] == CanidateName[x]:
                    CanidateVoteCnt[x] = CanidateVoteCnt[x] + 1
                    CanidateFound = True
                    
            # If canidate is not in list, add or append set vote count to one 
            if not CanidateFound:
                CanidateName.append(row[2])
                CanidateVoteCnt.append(1)
                CanidateCnt = CanidateCnt + 1
                                        
# Print Results to the screen

print(" ")
print("Election Results")
print("------------------------------")
print("Total Votes: " + str(TotalVotes))
print("------------------------------")

if CanidateCnt == 0:
    print(" ")
    print("*** No Canidates Found ***")
    print(" ")
else:
    # Print the list of Canidates and the Results
    for x in range(CanidateCnt):
        CanidatePcnt = CanidateVoteCnt [x] / TotalVotes
        print(CanidateName[x] + ": " + "{:.3%}".format(CanidatePcnt) + " (" + str(CanidateVoteCnt[x]) + ")") 
        if CanidatePcnt > MaxPcnt:
            MaxPcnt = CanidatePcnt
            WinnerSpot = x
    print("------------------------------")
    print("Winner: " + CanidateName[WinnerSpot])
    print("------------------------------")

print(" ")

# Save Results to a csv File.

output_path = os.path.join("..","PyPoll","analysis","results.csv")

with open(output_path, 'w', newline='') as csvfile:
    
    csvwriter = csv.writer(csvfile, delimiter=',')
    
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["------------------------------"])
    csvwriter.writerow(["Total Votes: " + str(TotalVotes)])
    csvwriter.writerow(["------------------------------"])
    
    if CanidateCnt == 0:
        csvwriter.writerow(" ")
        csvwriter.writerow("*** No Canidates Found ***")
        csvwriter.writerow(" ")
    else:
        # Print the list of Canidates and the Results
        for x in range(CanidateCnt):
            CanidatePcnt = CanidateVoteCnt [x] / TotalVotes
            csvwriter.writerow([CanidateName[x] + ": " + "{:.3%}".format(CanidatePcnt) + " (" + str(CanidateVoteCnt[x]) + ")"]) 
            if CanidatePcnt > MaxPcnt:
                MaxPcnt = CanidatePcnt
                WinnerSpot = x
        csvwriter.writerow(["------------------------------"])
        csvwriter.writerow(["Winner: " + CanidateName[WinnerSpot]])
        csvwriter.writerow(["------------------------------"]) 
