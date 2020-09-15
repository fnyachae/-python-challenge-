import os
import csv

# write the file path into a variable 
budget_csv_path = os.path.join("..", "Resource", "budget_data.csv")

# Open and read csv
with open(budget_csv_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    csv_header = next(csv_file)
    
    # Variable to hold total months 
    total_months = 0

    # the variable to hold list of dates from the csv file
    list_date = []

    # the variable to hold list of profit and losses from the csv file
    list_profits_losses = []

     # Read through each row of data after the header
    for row in csv_reader:
        total_months +=1

        list_date.append(row[0])

        list_profits_losses.append(row[1])
        
        
    print (total_months)

    print (list_date)

    print (list_profits_losses)
