import os

expenses = {} # stores expenses

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# I want the amount input to persist until either an int or float are entered
def add_expense():
    my_expense = input("Describe your expense: ")
    while True:
        amount = float(input("Enter the price of your expense: "))
        if not type(amount) == float or not type(amount) == int:
            pass
        else:
            if my_expense in expenses:
                expenses[my_expense] += amount
                exit()
            else:
                expenses[my_expense] = amount
                exit()
        print(f"Expense added to expense list!")

def view_expenses():
    if len(expenses) == 0:
        print("There are no expenses in your tracker! Add some by pressing 1")
    else:
        for key,value in expenses.items():
            if len(str(value)[str(value).index(".")+1:]) == 1:
                print(f"{key}: ${value:.2f}")
            else:
                print(f"{key}: ${int(value)}")

def calculate_expenses():
    total = 0
    if len(expenses) == 0:
        print("There are no expenses in your tracker! Add some by pressing 1")
    else:
        for expense in expenses.values():
            total += expense
        if len(str(total)[str(total).index(".")+1:]) == 1:
            print(f"The total of your expenses comes out to: ${total:.2f}")
        else:
            print(f"The total of your expenses comes out to: ${int(total)}")

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