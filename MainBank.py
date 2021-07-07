#dependencies
import os
import csv

#file  to output
file_to_load = "raw_data/budget_data.csv"
file_to_output = "analysis/budget_analysis.txt"

#set a path
budget_data = os.path.join("PyBank/Resources/budget_data.csv")

 # lists to store
Date = []
profit_amount = []
Monthly_Variation = []

# initialize variable
total_profit = 0
total_variation = 0
in_profit = 0

#Read the file
with open(budget_data, "r" ) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter= "," )
    header = next(csv_reader)
#The total number of months and the net total amount of "Profit/Losses" over the entire periode included in the dataset
    for row in csv_reader : 
            Date.append(row[0])
            profit_amount.append(row[1])
            num_months = len(Date)
            
    print("The number total of months in the dataset is", num_months)
    for i in range(len(profit_amount)):
      profit_amount [i] = int(profit_amount[i])
    print(profit_amount)
    total_profit = sum(profit_amount)
    print(total_profit)
    print("the net total amount of Profit/Losses in the dataset is $",total_profit)
    
#The average of the changes in "Profit/Losses" over the entire period
    for i in range(len(profit_amount)-1) :
        Monthly_Variation.append(profit_amount[i+1]-profit_amount[i])
        print(Monthly_Variation)
        avg_change = sum(Monthly_Variation)/(len(Monthly_Variation))
        avg_change= round(avg_change,2)
        print(avg_change)
        
        print("The average of the changes in Profit/Losses over the entire period is", avg_change )
        
#The greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(Monthly_Variation)
    Date_variation = (Monthly_Variation).index(greatest_increase) + 1
    increase_date =  Date[Date_variation]
    print(increase_date)
#The greatest decrease in losses (date and amount) over the entire period
    greatest_decrease = min(Monthly_Variation)
    Date_variation_inf = (Monthly_Variation).index(greatest_decrease) + 1
    decrease_date = Date[Date_variation_inf]
    print(greatest_decrease)
    print(decrease_date)

    output = (
    f"```text\n"
    f"Financial Analysis\n"
    f"---------------------------\n"
    f"Total Months: {num_months}\n"
    f"Total Revenue: ${total_profit}\n"
    f"Average Change: ${avg_change}\n"
    f"Greatest Increase in profits: {increase_date} (${greatest_increase})\n"
    f"Greatest Decrease in profis: {decrease_date} (${greatest_decrease})\n")
    f"```"
    #Print output to terminal
    print(output)

# Export the results to text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)