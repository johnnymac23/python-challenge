import os 
import csv

csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

total_months = 0
change = []
net_total = 0
biggest_increase = 0
biggest_decrease = 0
biggest_increase_month = ""
biggest_decrease_month = ""

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        total_months += 1
        profit = int(row[1])
        net_total += profit
        change.append(profit)


change = [change[i + 1] - change[i] for i in range(len(change) - 1)]


average_change = sum(change) / len(change)


biggest_increase = max(change)
biggest_decrease = min(change)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  
    
    for row in csvreader:
        if int(row[1]) == biggest_increase:
            biggest_increase_month = row[0]
        elif int(row[1]) == biggest_decrease:
            biggest_decrease_month = row[0]

print("Analysis")
print("Total MOnths:", total_months)
print("Total:", net_total)
print("Average Change:", average_change)
print("Greatest Increase in Profits:", biggest_increase_month, "($", biggest_increase, ")")
print("Greatest DEcrease in Profits:", biggest_decrease_month, "($", biggest_decrease, ")")




