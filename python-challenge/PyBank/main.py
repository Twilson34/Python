import csv
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(script_directory,'Resources/budget_data.csv')
output_file =os.path.join(script_directory,'Resources/budget_analysis.txt')

#opening and reading my input file titled budget_data.csv
with open(input_file, "r") as f_text:
    reader=csv.reader(f_text, delimiter= ",")
    csv_header=next(reader)
    previousrevenue=0

    i=0
    total=0
    netchanges=[]
    maxrevenueincrease=0
    maxrevenuedecrease=0
    greatestmonthincrease=0
    greatestmonthdecrease=0

    for info in reader:
        #The total number of months included in the dataset
        i+=1
        #Total Profit/Loss
        total += int(info[1])
        #Average profit loss per month
        currentPL= int(info[1]) - previousrevenue
        netchanges.append(currentPL)
        previousrevenue=int(info[1])
        #The greatest increase in profits (date and amount) over the entire period
        if currentPL > maxrevenueincrease:
            maxrevenueincrease= currentPL
            greatestmonthincrease=info[0]
         #The greatest decrease in losses (date and amount) over the entire period
        if currentPL < maxrevenuedecrease:
            maxrevenuedecrease= currentPL
            greatestmonthdecrease=info[0]

truelength=len(netchanges)-1
truetotal=sum(netchanges)-netchanges[0]

print(netchanges[0])

netmonthlyaverage= round(truetotal/truelength, 2)

output=(f"Financial Analysis\n"
f"------------------------\n"
f"Total Months: {i}\n"
f"Profit/Loss: ${total}\n"
f"Average Change:{netmonthlyaverage}\n"
f"Greatest Increase in Profits: {greatestmonthincrease} ${maxrevenueincrease}\n"
f"Greatest Decrease in Profits: {greatestmonthdecrease} ${maxrevenuedecrease}\n")

print(output)

with open(output_file, "w") as text:
        text.write(output)
