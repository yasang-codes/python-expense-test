import csv
import os

# Views the expenses.csv file and displays the expenses in a tabular format.

filePath = "expenses.csv"

def view_expenses():
    if not os.path.exists(filePath):
        print("No expenses found.")
        return "No expenses found. File does not exist."
    with open(filePath, "r") as file:
        reader = csv.reader(file)
        expenses = list(reader)        
        if len(expenses) == 2 and expenses[1] == []:
            print("No expenses found.")
            return "No expenses found. File is empty."
        count = 0
        for expense in expenses[1:]:            
            # check if the line is empty
            if not expense:
                continue
            # Ensure that the expense has all the required fields: Id, Date, Category, Amount, Description
            # Print 5 lines of expenses at a time. Ask the user to press enter to view the next 5 lines.            
            if len(expense) >= 5: 
                print("{:<12} {:<12} {:<12} {:<12} {:<12}".format(*expense))
                count += 1
                if count % 5 == 0:
                    input("Press Enter to view the next 5 expenses...")                    
        return expenses            
                      

            
