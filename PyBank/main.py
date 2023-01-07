#Import Modules / Libraries
import os
import csv

#Create an object
budget_data = os.path.join("Resources", "budget_data.csv")

total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

#Open and read the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Read the header row
    csv_header = next(csvreader)

    #Read the first row (tracking changes)
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])

    #Go through each row of data after the header and first row
    for row in csvreader:
        '''To Do:
        1. Create a list to capture all changes
        2. Find the max increase and max decrease
        3. Return values based on the indexes of
        '''
        #Keep track of the dates
        dates.append(row[0])

        #Calculate changes and add it to list of changes
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])

        #Calculate total number of months
        total_months += 1

        #Calculate total net amount of "Profits/Losses over the whole period"
        total_pl = total_pl + int(row[1])

    #Calculate the greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Calculate the greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Calculate the average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    
#Display information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")