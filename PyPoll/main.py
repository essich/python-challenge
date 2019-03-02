import os
import csv
import operator
#print(os.getcwd())

file_num = 1

candidatelist = []
uniquecand = []
candidateresult = {}


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
    winner = max(candidateresult.items(), key=operator.itemgetter(1))[0]
    print("Winner: " + winner)
 

    output_file = os.path.join('PYPoll_results' + str(file_num) +'.txt')
    
    with open(output_file, 'w') as txtfile:
        txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(votetotal) + 
          '\n-------------------------\n')
        for name in candidateresult:
            txtfile.writelines((str(name) +": " + str((votepercentage(int(count)))) +"% (" +str(candidateresult[name]) + ")"))
        txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

        with open(output_file, 'r') as readfile:
            print(readfile.read())
        
            
            
     

      