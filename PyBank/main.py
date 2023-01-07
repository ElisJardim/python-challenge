# Import Modules / Libraries
import os
import csv

# Create an object
budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")

total_months = 0
total_pl = 0
previous = 0
change = 0
dates = []
profits = []

# Open and read the CSV file
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Read the header row
    csv_header = next(csvreader)

    # Read the first row (tracking changes)
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    previous = int(first_row[1])

    # Go through each row of data after the header and first row
    for row in csvreader:
        # Keep track of the date
        dates.append(row[0])

        # Current profit/loss
        current_value = row[1]

        # Calculate changes and add it to list of changes
        change = int(current_value)-previous
        profits.append(change)

        # Calculate total number of months
        total_months += 1

        # Calculate total net amount of "Profits/Losses over the whole period"
        total_pl = total_pl + int(current_value)

        # Current value will be the previous value for the next line
        previous = int(current_value)


    # Calculate the greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    # Calculate the greatest decrease (lowest increase) in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    # Calculate the average change in "Profit/Losses between months over entire period"
    avg_change = sum(profits)/len(profits)
    

# Create a dictionary with the data that will be used in the result (reused for print and write to a file)
# Based on https://stackoverflow.com/questions/10112614/how-do-i-create-a-multiline-python-string-with-inline-variables
data = { 
    "total_months": str(total_months), 
    "total_pl": str(total_pl),
    "avg_change": str(round(avg_change,2)),
    "greatest_date": greatest_date,
    "greatest_increase": str(greatest_increase),
    "worst_date": worst_date,
    "greatest_decrease": str(greatest_decrease)
    }

# Create the output result
result = '''Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_pl}
Average Change: ${avg_change}
Greatest Increase in Profits: {greatest_date} (${greatest_increase})
Greatest Decrease in Profits: {worst_date} (${greatest_decrease})'''.format(**data)

# Display the result in the terminal
print(result)

# Save the result to a file
filename = os.path.join("PyBank", "analysis", "result.txt")
f = open(filename, "w")
f.write(result)
f.close()
