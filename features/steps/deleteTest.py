from behave import *
from src.add import add_expense
from src.read import read_expenses
from src.delete import delete_expense

@given('we have a sample expense to add and delete')
def step_impl(context):
    context.date = '01/01/2020'
    context.category = 'Food'
    context.amount = '100'
    context.description = 'Dinner'
    pass

@when('we try to delete it')
def step_impl(context):
    context.id = add_expense(context.date, context.category, context.amount, context.description)
    context.result = delete_expense(context.id)
    pass

@then('it should be deleted from expenses.csv')
def step_impl(context):
    expenses = read_expenses()
    # Check if the expense is in the list of expenses
    found = False
    for expense in expenses:
        if expense['Id'] == str(context.id):
            found = True
            break
    assert not found
    pass
    
    

