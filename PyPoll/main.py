import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

#The total number of votes cast
voterValue = 0

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

    for row in csvreader:
        if row[0] != "string":
            voterValue += 1
                
print(voterValue)

#A complete list of candidates who received votes
with open(csvpath, newline='') as csvfile:

    candidateList = csv.reader(csvfile, delimiter=',', skipinitialspace=True) 
    
    csv_header = next(candidateList)

    Candidate = []
    for row in candidateList:
        if row[2] not in Candidate:
            Candidate.append(row[2])  

print(Candidate) 

#The total number of votes each candidate won
khanVotes = 0
correyVotes = 0
liVotes = 0
tooleyVotes = 0
    
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        if row[2] == "Khan":
            khanVotes += 1
        elif row[2] == "Correy":
            correyVotes += 1
        elif row[2] == "Li":
            liVotes += 1
        elif row[2] == "O'Tooley":
            tooleyVotes += 1
                
                
print(f'Khan had {khanVotes} votes.')
print(f'Correy had {correyVotes} votes.')
print (f'Li had {liVotes} votes.')
print(f"O'Tooley had {tooleyVotes} votes.")

#The percentage of votes each candidate won

khanPercentage = round((khanVotes / voterValue) * 100,2)
correyPercentage = round((correyVotes / voterValue) * 100,2)
liPercentage = round((liVotes / voterValue) * 100,2)
tooleyPercentage = round((tooleyVotes / voterValue) * 100,2)

print(f'Khan won {khanPercentage}% of the votes.')
print(f'Correy won {correyPercentage}% of the votes.')
print(f'Li won {liPercentage}% of the votes.')
print(f"O'Tooley won {tooleyPercentage}% of the votes.")

#The winner of the election based on popular vote.
pollWinner = 0

pollResults = [khanVotes, correyVotes, liVotes, tooleyVotes]

for number in pollResults:
    if (int(number) > int(pollWinner)):
        pollWinner = number

if (int(pollWinner) == int(khanVotes)):
    print(f"The winner is Khan with {khanVotes} votes!")
elif (int(pollWinner) == int(correyVotes)):
    print(f"The winner is Correy with {correyVotes} votes!")
elif (int(pollWinner) == int(liVotes)):
    print(f"The winner is Li with {liVotes} votes!")
elif (int(pollWinner) == int(tooleyVotes)):
    print(f"The winner is Tooley with {tooleyVotes} votes!")

#Output to text file
f = open('electionResults.txt','a')
f.write("Election results")
f.write('\n' + "-------------------------")
f.write('\n' + f"Total votes: {voterValue}")
f.write('\n' + "-------------------------")
f.write('\n' + f"Khan: {khanPercentage}% ({khanVotes})")
f.write('\n' + f"Correy: {correyPercentage}% ({correyVotes})")
f.write('\n' + f"Li: {liPercentage}% ({liVotes})")
f.write('\n' + f"O'Tooley: {tooleyPercentage}% ({tooleyVotes})")
f.write('\n' + "-------------------------")
f.write('\n' + f"Winner: {pollWinner}")
f.write('\n' + "-------------------------")
f.close()