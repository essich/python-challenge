import os
import csv

print(os.getcwd())
Month=[]
PL=[]
openbudget = os.path.join("budgetdata.csv")

with open(openbudget, newline='') as csvfile:

   
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    print(csvreader)
    
    for data in csvreader:
        Month.append(data[0])
        PL.append(data[1])
        months = len(Month)
        netpl = sum(PL)
        maxpl = max(PL)
        print(maxpl)
        
        
        
        print("Month Total:" + str(months))
        print("Net ProfitLoss:" + str(netpl))
        print("Greatest Increase in Profits:" + str(netpl))
        print("Greatest Decrease in Profits:" + str(netpl))
        
        