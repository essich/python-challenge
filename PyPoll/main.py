import os
import csv

#print(os.getcwd())

candidatelist = []
uniquecand = []
#votespercand = []
#percentage = []
candidateresult = {}
#votetotal = 0

openelection = os.path.join("electiondata.csv")

with open(openelection, newline='') as csvfile:

   
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
  
    for data in csvreader:
        candidatelist.append(data[2])
        if data[2] not in uniquecand:
                uniquecand.append(data[2])
                
    print(str(uniquecand))

    candidateresult = {votes : 0 for votes in uniquecand}
    for cand in candidatelist:
             candidateresult[cand] += 1
    print(str(candidateresult))
    
    votetotal = len(candidatelist)

    def votepercentage(number):
        percentage = (number/votetotal)
        return round((percentage * 100))
    
    print("Election Results")
    print(" -------------------------")
    print("Total Votes:" + str(votetotal))
    for name in candidateresult:
        count = candidateresult[name]
        print((str(name) +": " + str((votepercentage(int(count)))) +"% (" +str(candidateresult[name]) + ")"))
    
    print ("-------------------------")
    print("Winner: " + max(candidateresult))
 # 
 # Khan: 63.000% (2218231)
 # Correy: 20.000% (704200)
 # Li: 14.000% (492940)
 # O'Tooley: 3.000% (105630)
 # -------------------------
 # Winner: Khan
 # -------------------------

        
            
            
     

      