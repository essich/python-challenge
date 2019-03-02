import os
import csv

Month=[]
PL=[]
MoMChange = []
openbudget = os.path.join("budgetdata.csv")

with open(openbudget, newline='') as csvfile:

   
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    
    for data in csvreader:
        Month.append(data[0])
        PL.append(int(data[1]))
    months = len(Month)
    netpl = sum(PL)
    
    for i in range(1,len(PL)):
        MoMChange.append(PL[i] - PL[i-1])
        avgreturn = round(sum(MoMChange)/len(MoMChange),2)
        maxplchg = max(MoMChange)
        minplchg = min(MoMChange)
        maxdate = Month[MoMChange.index(maxplchg)]
        mindate = Month[MoMChange.index(minplchg)]
    
    print("          "+"Financial Analysis of Budget")
            
    print("<------------------------------------------------------->")
    print("    "+"Month Total:" + str(months))
    print("    "+"Net ProfitLoss:" + str(netpl))
    print("    "+"Average Change:" + str(avgreturn))
    print("    "+"Greatest Increase in Profits:" + maxdate + " " + str(maxplchg))
    print("    "+"Greatest Decrease in Profits:" + mindate + " " + str(minplchg))
 
      
