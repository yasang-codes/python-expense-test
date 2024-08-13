import csv
import os

# Deletes an expense by its Id from the csv file.

filePath = "expenses.csv"

def delete_expense(id):
    if not os.path.exists(filePath):
        print("No expenses found.")
        return
    with open(filePath, "r") as file:
        reader = csv.reader(file)
        expenses = list(reader)
        if len(expenses) == 1:
            print("No expenses found.")
            return
        # Check if the ID exists in the file
        found = False
        for expense in expenses[1:]:
            if expense and int(expense[0]) == id:
                found = True
                expenses.remove(expense)
                break
        if not found:
            print("Expense not found.")
            return
    with open(filePath, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(expenses)
    print("Expense deleted successfully.")