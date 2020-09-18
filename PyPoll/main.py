import os
import csv

# # write the file path into a variable 
election_csv_path = os.path.join("resources" , "election_data.csv")

# # open and read cvs
with open (election_csv_path, 'r') as csvfile:
   csvreader = csv.reader(csvfile, delimiter = ",")

# Read the header row first
   csv_header = next(csvfile)

# the variable to hold total votes cast
   total_votes_cast = 0

# the variable to hold list of counties 
   list_county = []

# the variable to hold list of candidates 
   list_candidate = []


# the variable to hold list of voters names from the csv file
   list_voter = []

# Read through each row of data after the header
   for row in csvreader:

        total_votes_cast +=1

        list_voter.append(row[0])

        list_county.append(row[1])

        list_candidate.append(row[2])

print(total_votes_cast)

# to record the total cast voted 





   








   

