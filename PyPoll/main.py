import os
import csv

# write the file path into a variable 
election_csv_path = os.path.join("resources" , "election_data.csv")

# open and read cvs
with open (election_csv_path, 'r') as csvfile:
   csvreader = csv.reader(csvfile, delimiter = ",")

# Read the header row first
   csv_header = next(csvfile)

# the variable to hold vote count
   total_votez = 0

# the variable to hold winner vote count
   candidates_unique= []

# the variable to hold candicate  unique 
   candidate_vote_count = []

# read through each row of data  after the header 
   for row in csvreader:
      total_votez +=1

# get the reference to the candicate name from the row
      candidate_in = (row[2])

# if the candicate is in the list locate candicate by index  and increament the vote count by 1
      if candidate_in  in candidates_unique:
          candidate_index = candidates_unique.index(candidate_in)
          candidate_vote_count[candidate_index] = candidate_vote_count [candidate_index] + 1

      else:
# if the candidate was not on the candicate_unique list then append add 1 to vote count 
          candidates_unique.append(candidate_in)
          candidate_vote_count.append(1)

print(total_votez)
print(candidates_unique)
print(candidates_unique.index(candidate_in))

percentage = []
max_votez = candidate_vote_count[0]
max_index = 0

for x in range(len(candidates_unique)):
  # calculationto get the percentage , x will be a looper value
   vote_percentage = round((candidate_vote_count[x]/total_votez)*100, 2)
   percentage.append(vote_percentage)



   if candidate_vote_count[x] > max_votez:
         max_votez =candidate_vote_count[x]
         max_index = x

election_winner = candidates_unique[max_index]


print(candidate_vote_count)
print(max_votez)
print(election_winner)
print(percentage)





   

