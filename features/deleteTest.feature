Feature: testing the delete an expense function

  Scenario: delete a sample expense
    Given we have a sample expense to add and delete
        When we try to delete it 
            Then it should be deleted from expenses.csv