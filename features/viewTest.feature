Feature: testing the view expenses function

Scenario: viewing expenses from expenses.csv
    Given we have an expenses.csv file with at least one expense
        When we try to view expenses
            Then it should return expenses

Scenario: viewing expenses from expenses.csv
    Given we have no expenses.csv file
        When we try to view expenses with no file
            Then it should return message saying file does not exist

Scenario: viewing expenses from expenses.csv
    Given we have an expenses.csv file with no expenses
        When we try to view expenses in an empty file
            Then it should return message saying file is empty

