print("Welcome to the Simple Expense Tracker\n")
print("1. Add an Expense")
print("2. View Expenses")
print("3. Calculate Total Expenses")
print("4. Exit\n")
choice = print(input("Please choose an option (1-4): "))
expenses = []

def add_expense():
    my_expense = print(input("Enter your expense: "))
    expenses.append(my_expense)

def view_expenses():
    print(expenses)

def calculate_expenses():
    for expense in expenses:
        total += expense
    print(f"The total of your expenses comes out to: {total}")

def exit_program():
    exit

if choice == 1:
    add_expense()
elif choice == 2:
    view_expenses()
elif choice == 3:
    calculate_expenses()
elif choice == 4:
    exit_program()
else:
    print("Please enter a number from 1 to 4...")