# import dependencies
import csv, os

#create path to file
budgetdata = "/Users/saraharayratti/Desktop/python-challenge/PyBank/Resources/budget_data.csv"

#create variables
total_months = 0
changing_profit = 0
monthly_change = []
profit_variability = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]
total_profit = 0

#open as cvs file
with open(budgetdata) as profit_data:
    reader = csv.DictReader(profit_data)

    for row in reader:

        # total of months
        total_months = total_months + 1
        total_profit = total_profit + int(row["Profit/Losses"])

        #total profit
        net_profit= int(row["Profit/Losses"]) - changing_profit
        changing_profit = int(row["Profit/Losses"])
        profit_variability = profit_variability + [net_profit]
        monthly_change = monthly_change + [row["Date"]]

        # greatest increase
        if (net_profit> greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = net_profit

        # greatest decrease
        if (net_profit < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = net_profit


profit_avg = sum(profit_variability) / len(profit_variability)

#create analysis and print it
analysis = (
    f"\nFinancial Analysis\n"
    f"Total Months: {total_months}\n"
    f"Total Profit: ${total_profit}\n"
    f"Average Change: ${profit_avg}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

print (analysis)

#create path to txt file and export it:
analysistxt = "/Users/saraharayratti/Desktop/python-challenge/PyBank/analysis/analysis_bank.txt"

with open(analysistxt, "w") as txt_file:
    txt_file.write(analysis)

