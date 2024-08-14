# import add_expense function from add.py
from src.add import add_expense

# import view_expenses function from view.py
from src.view import view_expenses

# import delete_expense function from delete.py
from src.delete import delete_expense

# import validate_date function from validate.py
from src.validations import validate_date

# import validate_amount function
from src.validations import validate_amount

# import validate_category function
from src.validations import validate_category

# import validate_description function 
from src.validations import validate_description

import keyboard

# Welcome the user and ask them to choose an input form list of options
def show_menu():
    print("Welcome to the Personal Expense Tracker!")
    print("Please choose an option from the list below:")
    print("1. Add an expense")
    print("2. View expenses")
    print("3. Delete an expense")
    print("4. Exit")

def show_return_to_menu():
    print("Done Viewing? Press Esc to exit. Press any other key to return to the main menu.")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            if event.name == 'esc':
                return False
            else:                  
                return True
         
def main():

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Add an expense")
            date = input("Enter the date of the expense (DD/MM/YYYY): ")
            # Add a check to ensure that the date is in the correct format and is a valid date.
            while not validate_date(date):
                date = input("Invalid date format. Please enter the date of the expense (DD/MM/YYYY): ")
            category = input("Enter the category of the expense: ")
            # Add a check to ensure that the category is not empty.
            while not validate_category(category):
                category = input("Invalid category. Please enter the category of the expense: ")
            amount = input("Enter the amount of the expense: ")
            # Add a check to ensure that the amount is a valid number and is greater than 0.
            while not validate_amount(amount):
                amount = input("Invalid amount. Please enter the amount of the expense: ")
            description = input("Enter a description for the expense: ")
            # Add a check to ensure that the description is not empty.
            while not validate_description(description):
                description = input("Invalid description. Please enter a description for the expense: ")
            result = add_expense(date, category, amount, description)
            if isinstance(result, int):
                print(f"Expense added successfully. Expense ID: {result}")
            else:
                print(f"Error: {result}")
        elif choice == "2":
            print("View expenses")
            view_expenses()            
            if show_return_to_menu():
                # Clear the input
                keyboard.send("backspace")           
                continue
            else:
                print("Bye!")
                break                              
        elif choice == "3":
            print("Delete an expense")
            view_expenses()   
            id = input("Enter the ID of the expense to delete: ")
            delete_expense(int(id))
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()