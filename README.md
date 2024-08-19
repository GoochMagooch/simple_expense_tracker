# simple_expense_tracker
You’ve been asked to build a basic expense tracker for an employee to track their expenses. The system will allow users to add expenses, view a list of expenses, and calculate the total amount spent.

Challenge Requirements:
Data Structure:
Create a list called expenses that will store each expense as a tuple containing the expense description (e.g., "Lunch") and the expense amount (e.g., 12.50).

Add Expense:
Write a function add_expense(description, amount) that adds a new expense to the expenses list.

View Expenses:
Write a function view_expenses() that prints out each expense in the list in a readable format, showing the description and amount for each expense.

Calculate Total Expenses:
Write a function calculate_total() that calculates and returns the total amount spent based on the expenses stored in the list.

Main Program:
Write a simple main program that:

Displays a menu with options to add an expense, view all expenses, calculate total expenses, or exit.
Repeats until the user chooses to exit.
Additional Parameters:
Input Validation: Ensure that the user inputs valid numerical amounts for the expenses.
Edge Cases: Handle cases where there are no expenses to display or calculate.
Clear Output: Ensure that expenses are displayed clearly and the total is properly formatted.

Example Usage:
Welcome to the Simple Expense Tracker

1. Add an Expense
2. View Expenses
3. Calculate Total Expenses
4. Exit

Please choose an option (1-4):
Option 1: User can add an expense by providing a description and amount.
Option 2: User can view all logged expenses.
Option 3: User can calculate and see the total amount of expenses.
Option 4: Exits the program.

Expected Outcome:
This challenge tests your ability to work with lists, write multiple functions, handle basic user input, and build a simple program that mimics an everyday task of tracking expenses.