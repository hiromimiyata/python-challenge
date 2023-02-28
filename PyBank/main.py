import csv
import os

#Opens the csv file
csvpath = os.path.join("..","Instructions", "PyBank", "Resources", "budget_data.csv")

#Variables
x = 0
profit = 0
average = 0
lst=[]
value = 0
originalvalue = 0 
First=True
count=0
maxindexdate=0
minindexdate=0 
new = []
#opening path
with open(csvpath) as csvfile:
    csvreader = csv.reader( csvfile, delimiter= ',')

    print("Financial Analysis")
    print("----------------------------")
     

    #loop
    for row in csvreader:
        new = new + row
        if row[0] != 'Date':
            x = x + 1
            profit = profit + int(row[1])
        if First == True and row[1] != "Profit/Losses":
            First= False
            originalvalue = int(row[1])
        elif row[1] != "Profit/Losses":
            value =  int(row[1]) - originalvalue
            lst.append(value)
            originalvalue = int(row[1])
        
    finalprofit = "${:}".format(profit)
    averagechange =  "${:}".format(round((sum(lst)/len(lst)),2))
    increase = "${:}".format(max(lst))
    decrease = "${:}".format(min(lst))
    indexmax = int((lst.index(max(lst))) )+ 2
    indexmin = int((lst.index(min(lst)))) + 2

    
    maxindexdate = new[indexmax*2]
    minindexdate = new[indexmin*2]

    #printing answers
    print("Total Months:",x)
    print("Total:",finalprofit)
    print("Average Change:", averagechange)
    print("Greatest Increase in Profits:", maxindexdate, "(",increase,")")
    print("Greatest Decrease in Profits:", minindexdate, "(",decrease,")")
    
#exporting terminal output to txt
import sys
exp = os.path.join("..","Instructions", "analysis","testresults.txt")
f = open(exp, 'w')
sys.stdout = f
print("Financial Analysis")
print("----------------------------")
print("Total Months:",x)
print("Total:",finalprofit)
print("Average Change:", averagechange)
print("Greatest Increase in Profits:", maxindexdate, "(",increase,")")
print("Greatest Decrease in Profits:", minindexdate, "(",decrease,")")
f.close()