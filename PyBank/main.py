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
        
    # Variable to hold The net total amount of "Profit/Losses" over the entire period
    net_profit_loss = 0

    # the variable to hold list of changes in "Profit/Losses" 
    list_changes = []

    # variable to hold previous "Profit/Losses" 
    previous_p_l = 0    

    # loop through each value in list_profits_losses
    for amount in list_profits_losses:
        net_profit_loss += int(amount)

        if previous_p_l == 0:   
            previous_p_l = int(amount)
        else:
            list_changes.append(int(amount)-previous_p_l)
            previous_p_l = int(amount)
      
    # variable to hold the average of the changes in "Profit/Losses" over the entire period
    average_changes = round((int(list_profits_losses[total_months-1])-int(list_profits_losses[0]))/(total_months-1),2)
       
    # variable to hold the greatest increase in profits (date and amount) over the entire period
    greatest_profit = max(list_changes)

    # variable to hold the month with the greatest increase in profits (date and amount) over the entire period
    greatest_profit_month = list_date[list_changes.index(greatest_profit)+1]        
    
    # variable to hold the greatest decrease in profits (date and amount) over the entire period
    greatest_loss = min(list_changes)

    # variable to hold the month with the greatest decrease in profits (date and amount) over the entire period
    greatest_loss_month = list_date[list_changes.index(greatest_loss)+1]

    
    
