# pseudocode - to create models or flowcharts for a programs
# Indirect part
import os
dir(os)
print(dir(os))
dir(os.path)

# Open the data file. data we need to retrieve - direct path
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file
with open(file_to_load) as election_data:
    # Print the file object.
     print(election_data)


# Create a filename variable to a direct or indirect path to the file. - this creates a txt file and writes hello world to the txt file
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")
# Close the file
outfile.close()


# Create a filename variable to a direct or indirect path to the file. cleaner and more concise code
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    #txt_file.write("Hello World")
  # Write three counties to the file. - separate with commas to space the counties
     #txt_file.write("Arapahoe, ")
     #txt_file.write("Denver, ")
    # txt_file.write("Jefferson")
     # Use above or below codes to add counties
    #txt_file.write("Arapahoe, Denver, Jefferson")
     # Write three counties to the file.
          txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")


# 3.4.4 Read the Election Results
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
        # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
        # print(row[0]) to retrieve the first item from each row
        # Read and print the header row.
    headers = next(file_reader)
    print(headers)





    # Write down the names of all the candidates - a complete list of  candidate
    # Add a vote count for each candidate.- total number of vote cast
    # Get the total votes for each candidate. - the percentage of votes each candidate won
    # Get the total votes cast for the election. - total number of votes each candidate won
    # The winner of the election based on the popular vote
    # 
    # 1. The  total number of vote cast
    # 2. A complete list of  candidate 
    # 3. The percentage of votes each candidate won
    # 4. The total number of votes each candidate won
    # 5. The winner of the election based on the popular vote












# Dependencies Dependencies are modules and packages, or a programming script that someone else has written, that allows you to increase the functional programming of your code, or speed and efficiency
# Import the datetime class from the datetime module.
#import datetime
# Use the now() attribute on the datetime class to get the present time.
#now = datetime.datetime.now()
# Print the present time.
#print("The time right now is ", now)

# Dependencies - Modules
