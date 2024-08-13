# Reads expenses from the expenses.csv file and returns them as a list of dictionaries.

import os
import csv

filePath = "expenses.csv"

def read_expenses():
    if not os.path.exists(filePath):
        return []
    with open(filePath, "r") as file:
        reader = csv.DictReader(file)
        expenses = list(reader)
        return expenses