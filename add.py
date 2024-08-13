import csv
import os
import datetime

def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d/%m/%Y')
        return True
    except ValueError:
        return False

# Adds an expense to the database and saves as a CSV file.

filePath = "expenses.csv"

def add_expense():
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
    
    date = input("Enter the date of the expense (DD/MM/YYYY): ")
    # Add a check to ensure that the date is in the correct format and is a valid date.
    while not validate_date(date):
        date = input("Invalid date format. Please enter the date of the expense (DD/MM/YYYY): ")

    category = input("Enter the category of the expense: ")
    amount = input("Enter the amount of the expense: ")
    description = input("Enter a description for the expense: ")

    with open(filePath, "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, date, category, amount, description])



