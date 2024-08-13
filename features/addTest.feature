Feature: testing the add an expense function

  Scenario: add a sample expense
    Given we have a sample expense
        When we try to add it 
            Then it should be added to expenses.csv