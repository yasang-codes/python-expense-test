import csv
import os


# Adds an expense to the database and saves as a CSV file.

filePath = "expenses.csv"

def add_expense(date, category, amount, description):
    if not os.path.exists(filePath):
        with open(filePath, "w") as file:
            writer = csv.writer(file)
            writer.writerow(["Id", "Date", "Category", "Amount", "Description"])
    
    # Generate a unique ID for the expense. Generate a new ID by incrementing the last ID in the file. If no ID is present, start from 1.
    with open(filePath, "r") as file:
        reader = csv.reader(file)
        expenses = list(reader)
        # Read last line of the file to get the last ID
        if len(expenses) > 1:
            try:
                last_id = int(expenses[-1][0])
            except (ValueError, IndexError):
                last_id = 0
        else:
            last_id = 0
        id = last_id + 1  
    

    with open(filePath, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, date, category, amount, description])



