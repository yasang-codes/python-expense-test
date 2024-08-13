from behave import *
from src.add import add_expense
from src.read import read_expenses

@given('we have a sample expense')
def step_impl(context):
    context.date = '01/01/2020'
    context.category = 'Food'
    context.amount = '10'
    context.description = 'Lunch'
    pass

@when('we try to add it')
def step_impl(context):
    context.result = add_expense(context.date, context.category, context.amount, context.description)
    pass

@then('it should be added to expenses.csv')
def step_impl(context):
    expenses = read_expenses()
    # Check if the expense is in the list of expenses
    found = False
    for expense in expenses:
        if expense['Date'] == context.date and expense['Category'] == context.category and expense['Amount'] == context.amount and expense['Description'] == context.description:
            found = True
            break
    assert found
    pass

