from behave import *
from src.add import add_expense

@given('we have a sample expense with valid values')
def step_impl(context):
    context.date = '01/01/2020'
    context.category = 'Food'
    context.amount = '10'
    context.description = 'Lunch'
    pass

@when('we try to add the expense with valid values')
def step_impl(context):
    context.result = add_expense(context.date, context.category, context.amount, context.description)
    pass

@then('it should be added to expenses.csv and return the id')
def step_impl(context):
    # If result is an integer, it means the expense was added successfully
    if isinstance(context.result, int):
        assert True
    else:
        assert False  
    pass

# Second scenario

@given('we have a sample expense with incorrect date format')
def step_impl(context):
    context.date = '01-01-2020'
    context.category = 'Food'
    context.amount = '10'
    context.description = 'Lunch'
    pass

@when('we try to add the expense with incorrect date format')
def step_impl(context):
    context.result = add_expense(context.date, context.category, context.amount, context.description)
    pass

@then('it should return an error message for incorrect date format')
def step_impl(context):
    if(context.result == "Invalid date format. Date must be in the format (DD/MM/YYYY)."):
        assert True
    else:
        assert False
    pass

# Third scenario

@given('we have a sample expense with incorrect amount')
def step_impl(context):
    context.date = '01/01/2020'
    context.category = 'Food'
    context.amount = 'abc'
    context.description = 'Lunch'
    pass

@when('we try to add the expense with incorrect amount')
def step_impl(context):
    context.result = add_expense(context.date, context.category, context.amount, context.description)
    pass

@then('it should return an error message for incorrect amount')
def step_impl(context):
    if(context.result == "Invalid amount. Amount must be a valid number greater than 0."):
        assert True
    else:
        assert False
    pass

# Fourth scenario

@given('we have a sample expense with empty category')
def step_impl(context):
    context.date = '01/01/2020'    
    context.amount = '10'
    context.category = ''
    context.description = 'Lunch'
    pass

@when('we try to add the expense with empty category')
def step_impl(context):
    context.result = add_expense(context.date, context.category, context.amount, context.description)
    pass

@then('it should return an error message for empty category')
def step_impl(context):
    if(context.result == "Invalid category. Category cannot be empty."):
        assert True
    else:
        assert False
    pass

# Fifth scenario
@given('we have a sample expense with empty description')
def step_impl(context):
    context.date = '01/01/2020'
    context.category = 'Food'
    context.amount = '10'
    context.description = ''
    pass

@when('we try to add the expense with empty description')
def step_impl(context):
    context.result = add_expense(context.date, context.category, context.amount, context.description)
    pass

@then('it should return an error message for empty description')
def step_impl(context):
    if(context.result == "Invalid description. Description cannot be empty."):
        assert True
    else:
        assert False
    pass





