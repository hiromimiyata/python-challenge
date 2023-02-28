import csv
import os

#Opens the csv file
csvpath = os.path.join("..","Instructions", "PyPoll", "Resources", "election_data.csv")

#variables
votes = 0
prevrowvoter = 0
first = True
veryfirst=True
count = 0
names = []
votelst = []
zippedup = 0
finalistnames = {}

#reading the csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader( csvfile, delimiter= ',')

    print("Election Results")
    print("----------------------------") 

#loop
    for row in csvreader:
        if row[0].isnumeric()==True:
            votes = votes + 1
        if row[0].isnumeric()==True and first == True and veryfirst == True:
            first = False
            veryfirst= False
            prevrowvoter = row[2]
            count = 0
            names.append(prevrowvoter)
        elif row[0].isnumeric()==True and first == True:
            first = False
            prevrowvoter = row[2]
            count = count + 1
            names.append(prevrowvoter)
        elif row[0].isnumeric()==True and prevrowvoter == row[2]:
            count = count + 1
        elif row[0].isnumeric()==True and prevrowvoter != row[2]:
            count = count + 1
            votelst.append(count)
            names.append(row[2])
            prevrowvoter = row[2]
            count = 0
    votelst.append(count)

    votelst[-1] = votelst[-1] + 1

#combining the names and the votes into a zip and adding the votes for the candidates
    zippedup = zip(names, votelst)  
    for x, y in zippedup:
        if x in finalistnames :
            finalistnames[x] += y
        else :
            finalistnames[x] = y
    
#printing total votes on terminal
    print ("Total Votes:", votes)
    print("----------------------------") 

#printing results from the zip and calculating the percentage of votes and returning in percentage format
for x in finalistnames:
     print (x,":", "{:.3%}".format(finalistnames[x]/votes), "(",finalistnames[x], ")")

#printing the person with the most votes
print("----------------------------") 
print("Winner:",max(finalistnames,key=finalistnames.get))
print("----------------------------") 
#exporting results in testresults2.txt in analysis folder
import sys
exp = os.path.join("..","Instructions", "analysis","testresults2.txt")
f = open(exp, 'w')
sys.stdout = f
print("Election Results")
print("----------------------------") 
print ("Total Votes:", votes)
print("----------------------------") 
for x in finalistnames:
    print (x,":", "{:.3%}".format(finalistnames[x]/votes), "(",finalistnames[x], ")")
print("----------------------------") 
print("Winner:",max(finalistnames,key=finalistnames.get))
print("----------------------------") 
f.close()