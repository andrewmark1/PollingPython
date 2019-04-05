# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:19:08 2019

@author: andrewd
"""

import os
import csv

voterid = []
county = []
candidate = []
votes = []
totalVotes = 0

csvpath = os.path.join("..","..","..","UCBBEL201902DATA2","03-Python","Homework","Instructions","PyPoll","Resources","election_data.csv")
outputpath = os.path.join(".","output.txt")

with open(csvpath, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    
    for row in csvreader:
        voterid.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

data = zip(voterid,county,candidate)

totalVotes = len(candidate)
candidateList = list(set(candidate))

votes = [0] * len(candidateList)


#count the votes!
for name in candidate:
    votes[candidateList.index(name)] += 1
    
with open(outputpath, 'w') as textfile:
    textfile.write("""Election Results
-----------------
Total Votes: {:,}
-----------------""".format(totalVotes))
    for name in candidateList:
        textfile.write("\n{}: {:.3%} ({:,}))".format(name,votes[candidateList.index(name)]/totalVotes,votes[candidateList.index(name)]))
    
    textfile.write("""\n-----------------
Winner: {}
-----------------""".format(candidateList[votes.index(max(votes))])   
)    
    
#print results to console

print("""Election Results
-----------------
Total Votes: {:,}
-----------------""".format(totalVotes))

for name in candidateList:
    print("{}: {:.3%} ({:,}))".format(name,votes[candidateList.index(name)]/totalVotes,votes[candidateList.index(name)]))
    
print("""-----------------
Winner: {}
-----------------""".format(candidateList[votes.index(max(votes))])   
)    