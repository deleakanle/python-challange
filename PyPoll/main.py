# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("analysis", "election_analysis.txt")

# Initialize variables, lists and dictionaries to track the election data
total_votes = 0

candidate_dictionary = {}

# Winning Candidate and Winning Count Tracker
max_votes = 0
winner = ''

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

         # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        # If the candidate is not already in the candidate list, add them
        if row[2] in candidate_dictionary.keys():
            candidate_dictionary[row[2]] += 1
        # Add a vote to the candidate's count
        else:
           candidate_dictionary[row[2]] = 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
    # Generate the winning candidate summary
    output = '\nElection Results\n'
    output += '----------------------------\n'
    output += f'Total Votes: {total_votes}]\n'
    output += '----------------------------\n'
    for candidate in candidate_dictionary:
        output += f'{candidate} : {(candidate_dictionary[candidate]/total_votes)*100:.3f}% ({candidate_dictionary[candidate]})\n'
        if candidate_dictionary[candidate] > max_votes:
            winner = candidate
            max_votes = candidate_dictionary[candidate]
    output += '----------------------------\n'
    output += f'Winner: {winner}\n'
    output += '----------------------------\n'

    # Print the total vote count (to terminal)
    print(output)

    # Save the winning candidate summary to the text file
    txt_file.write(output)