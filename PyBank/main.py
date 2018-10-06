import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
monthValue = 0
profitloss = 0
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

# Determine the total numbers of months
    for row in csvreader:
            if row[0] != "string":
                monthValue += 1
    monthValue -= 1
    #print(monthValue) 
print(f"Number of months: {monthValue}")

# Determine the total net amount of “Profit/Losses” over the entire period
netProfit = 0
    
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

    # Print(netProfit)
    for row in csvreader:
        netProfit = netProfit + int(row[1])
        
    #print(netProfit / monthValue)
print(f"Net profit: ${netProfit}")

# Determine the average change in “Profit/Losses” between months over the entire period 
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    firstRow = next(csvreader)

    for row in firstRow:
        firstValue = row
        
    for row in csvreader:
        lastValue = row[1]
        
averageChange = (int(firstValue) - int(lastValue)) / (int(monthValue) - 1)

#Print(averageChange)
print(f"Average Change: ${averageChange}")

# Determine greatest increase in profits (date and amount) over the entire period
greatestDifference = 0
previousValue = 0

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    for row in csvreader:
        currentValue = int(row[1])
        
        valueDifference = (currentValue - previousValue)
        if (valueDifference > greatestDifference):
            greatestDifference = valueDifference
            differenceMonth = row[0]
        previousValue = int(row[1])
            
#print(greatestDifference)
print(f"Greatest increase in profits: ${greatestDifference} on {differenceMonth}")

#Determine the greatest decrease in losses (date and amount) over the entire period

greatestLoss = 0
previousValue = 0

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)

    for row in csvreader:
        currentValue = int(row[1])
        
        valueDifference = (previousValue - currentValue)
        if (valueDifference > greatestLoss):
            greatestLoss = valueDifference
            lossMonth = row[0]
        previousValue = int(row[1])
        
greatestLoss = greatestLoss - (greatestLoss * 2)
ß
#Write to .txt
f = open('bankResults.txt','a')
f.write("Financial Analysis")
f.write('\n' + "-------------------------")
f.write('\n' + f"Number of months: {monthValue}")
f.write('\n' + f"Total: ${netProfit}")
f.write('\n' + f"Average Change: ${averageChange}")
f.write('\n' + f"Greatest increase in Profits: ${greatestDifference} on {differenceMonth}")
f.write('\n' + f"Greatest decrease in profits: ${greatestLoss} on {lossMonth}")
f.close()