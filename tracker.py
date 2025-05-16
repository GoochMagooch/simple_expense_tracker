import os

expenses = {} # stores expenses

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def add_expense():
    my_expense = input("Describe your expense: ")
    amount = int(input("Enter your expense: "))
    expenses[my_expense] = amount
    print(f"Expense added to expense list!")

def view_expenses():
    for key,value in expenses.items():
        print(f"{key}: ${value}")

def calculate_expenses():
    total = 0
    for expense in expenses.values():
        total += expense
    print(f"The total of your expenses comes out to: ${total}")

def exit_program():
    print("Exiting Expense Tracker...Goodbye")
    exit()

print("Welcome to the Simple Expense Tracker\n")
print("1. Add an Expense")
print("2. View Expenses")
print("3. Calculate Total Expenses")
print("\"Menu\" to bring up menu")
print("\"Exit\" to exit\n")

while True:
    choice = input("Please choose an option (1 - 3), \"menu\", or \"exit\": ")

    if choice.lower() == "exit":
        print("Are you sure you want to exit?")
        exit_choice = input("Press \"Y\" or \"N\": ")
        if exit_choice.lower() == "y":
            exit_program()
        else:
            clear_screen()
            pass
    elif choice.lower() == "menu":
        clear_screen()
        print("1. Add an Expense")
        print("2. View Expenses")
        print("3. Calculate Total Expenses")
        print("\"Menu\" to bring up menu")
        print("\"Exit\" to exit\n")
    else:
        try:
            int_choice = int(choice)
            if int_choice == 1:
                clear_screen()
                add_expense()
            elif int_choice == 2:
                clear_screen()
                view_expenses()
            elif int_choice == 3:
                clear_screen()
                calculate_expenses()
            else:
                clear_screen()
                pass
        except ValueError:
            clear_screen()
            pass