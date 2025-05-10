import os

expenses = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_expense():
    description = input("Describe your expense: ")
    amount = int(input("Enter your expense: "))
    print(f"Expense: {description}, Amount: {amount}")

def view_expenses():
    print(expenses)

def calculate_expenses():
    total = 0
    for expense in expenses:
        total += expense
    print(f"The total of your expenses comes out to: {total}")

def exit_program():
    print("Exiting Expense Tracker...Goodbye")

while True:

    print("Welcome to the Simple Expense Tracker\n")
    print("1. Add an Expense")
    print("2. View Expenses")
    print("3. Calculate Total Expenses")
    print("4. Exit\n")
    choice = input("Please choose an option (1 - 4) or \"exit\": ")

    if choice == "exit":
        clear_screen()
        exit_program()
        exit()
    else:
        try:
            int_choice = int(choice)
            if int_choice == 1:
                add_expense()
                clear_screen() # Clears screen after a choice is made
                # function to reinitialize menu
            elif int_choice == 2:
                view_expenses()
            elif int_choice == 3:
                calculate_expenses()
            elif int_choice == 4:
                clear_screen()
                exit_program()
                exit
            else:
                print("Please enter a number from 1 to 4 or \"exit\"")
        except ValueError:
            print("Please enter a number from 1 to 4 or \"exit\"")