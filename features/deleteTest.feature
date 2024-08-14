Feature: testing the delete an expense function

  Scenario: delete a sample expense
    Given we have a sample expense to add and delete
        When we try to delete it 
            Then it should be deleted from expenses.csv

  Scenario: delete a sample expense with incorrect id
    Given we have a sample expense to add and delete with incorrect id
        When we try to delete it using an incorrect id
            Then it should not be deleted from expenses.csv          