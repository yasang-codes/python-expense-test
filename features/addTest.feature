Feature: testing the add an expense function

  Scenario: add a sample expense
    Given we have a sample expense with valid values
        When we try to add the expense with valid values
            Then it should be added to expenses.csv and return the id 

  Scenario: add a sample expense with incorrect date format
    Given we have a sample expense with incorrect date format
        When we try to add the expense with incorrect date format
            Then it should return an error message for incorrect date format       

  Scenario: add a sample expense with incorrect amount
    Given we have a sample expense with incorrect amount
        When we try to add the expense with incorrect amount
            Then it should return an error message for incorrect amount  

  Scenario: add a sample expense with empty category
    Given we have a sample expense with empty category
        When we try to add the expense with empty category
            Then it should return an error message for empty category  

  Scenario: add a sample expense with empty description
    Given we have a sample expense with empty description
        When we try to add the expense with empty description
            Then it should return an error message for empty description                         
            
