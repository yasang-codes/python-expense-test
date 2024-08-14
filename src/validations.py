import datetime

def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d/%m/%Y')
        return True
    except ValueError:
        return False
    
def validate_amount(amount):
    # Check if the amount is a valid number and is greater than 0
    try:
        amount = float(amount)
        if amount > 0:
            return True
        else:
            return False
    except ValueError:
        return False
    
def validate_category(category):
    # Check if the category is not empty
    if category:
        return True
    else:
        return False

def validate_description(description):
    # Check if the description is not empty
    if description:
        return True
    else:
        return False        
        
       
        