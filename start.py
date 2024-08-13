# import add_expense function from add.py
from add import add_expense

# import view_expenses function from view.py
from view import view_expenses

# import delete_expense function from delete.py
from delete import delete_expense

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
            add_expense()
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