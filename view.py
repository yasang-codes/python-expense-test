import csv
import os

# Views the expenses.csv file and displays the expenses in a tabular format.

filePath = "expenses.csv"

def view_expenses():
    if not os.path.exists(filePath):
        print("No expenses found.")
        return
    with open(filePath, "r") as file:
        reader = csv.reader(file)
        expenses = list(reader)
        if len(expenses) == 1:
            print("No expenses found.")
            return
        for expense in expenses[1:]:
            # check if the line is empty
            if not expense:
                continue
            # Ensure that the expense has all the required fields: Id, Date, Category, Amount, Description
            if len(expense) >= 5: 
                print("{:<12} {:<12} {:<12} {:<12} {:<12}".format(*expense))            

