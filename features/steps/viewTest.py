from behave import *
from src.view import view_expenses
from src.add import add_expense
import os
import csv

@given('we have an expenses.csv file with at least one expense')
def step_impl(context):
    # delete the file if it exists
    if os.path.exists('expenses.csv'):
        os.remove('expenses.csv')
    context.date = '01/01/2020'
    context.category = 'Food'
    context.amount = '10'
    context.description = 'Lunch'
    context.id = add_expense(context.date, context.category, context.amount, context.description)
    pass

@when('we try to view expenses')
def step_impl(context):
    context.result = view_expenses()
    pass

@then('it should return expenses')
def step_impl(context):
    # Result must be list of string lists: list[list[str]]     
    assert type(context.result) == list
    assert type(context.result[-1]) == list
    assert type(context.result[-1][0]) == str 
    # Check if the last expense in the file is the one we added
    context.result.reverse()     
    assert context.result[0][1] == context.date
    assert context.result[0][2] == context.category
    assert context.result[0][3] == context.amount
    assert context.result[0][4] == context.description
    pass

# Second scenario
@given('we have no expenses.csv file')
def step_impl(context):
    # delete the file if it exists
    if os.path.exists('expenses.csv'):
        os.remove('expenses.csv')
    pass

@when('we try to view expenses with no file')
def step_impl(context):
    context.result = view_expenses()
    pass

@then('it should return message saying file does not exist')
def step_impl(context):
    if(context.result == "No expenses found. File does not exist."):
        assert True
    else:
        assert False

# Third scenario

@given('we have an expenses.csv file with no expenses')
def step_impl(context):
    # delete the file if it exists
    if os.path.exists('expenses.csv'):
        os.remove('expenses.csv')        
    with open('expenses.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(["Id", "Date", "Category", "Amount", "Description"])
    pass        

@when('we try to view expenses in an empty file')
def step_impl(context):
    context.result = view_expenses()
    pass

@then('it should return message saying file is empty')
def step_impl(context):
    if(context.result == "No expenses found. File is empty."):
        assert True
    else:
        assert False
    pass


