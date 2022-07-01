#Data Source
import csv 
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Open the election results and read file
#with open(file_to_load) as election_data:

  #      print(election_data)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")
#Use the with statement to open the file

#Open the election results and read file
with open(file_to_load) as election_data:

#with open(file_to_save,"w") as txt_file:
       # txt_file.write("Arapahoe \nDenver\nJefferson")
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
     # Print each row in the CSV file.
    #for row in file_reader:
        #print(row)
    headers = next(file_reader)
    print(headers)
