# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")
file_to_output = os.path.join("analysis", "budget_analysis.txt")

# Define variables to track the financial data
total_months = 0
total_net = 0
total_profit_and_losses = 0
previous_profit = 0
max_month = ''
max_change = 0
min_month = ''
min_change = 0

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:

        # Track the total months
        total_months += 1

        # Track the total net change
        total_net += int(row[1])

        # Calculate the greatest increase and decrease in profits (month and amount)
        if previous_profit == 0:
            previous_profit = int(row[1])
        else:
            change = int(row[1]) - previous_profit
            total_profit_and_losses += change
            previous_profit = int(row[1])
            if change > max_change:
                max_month = row[0]
                max_change = change
            if change < min_change:
                min_month = row[0]
                min_change = change

with open(file_to_output, "w") as txt_file:

    # Generate the output summary
    output = 'Financial Analysis\n'
    output += '----------------------------\n'
    output += f'Total Months: {total_months}\n'
    output += f'Total: ${total_net}\n'
    output += f'Average Change: ${total_profit_and_losses/(total_months-1):.2f}\n'
    output += f'Greatest Increase in Profits: {max_month} (${max_change})\n'
    output += f'Greatest Decrease in Profits: {min_month} (${min_change})\n'

    # Print the output
    print(output)

    # Write the results to a text file
    txt_file.write(output)
