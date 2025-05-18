import os
import csv

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Adds/updates Expenses in expenses.csv
def add_expense():
    # Separates expenses file into expense and amount
    with open("expenses.csv") as x:
        expenses_file = csv.reader(x, delimiter=',')
        expense = []
        amount = []
        for i in expenses_file:
            expense.append(i[0])
            amount.append(float(i[1]))

    # Defines list of formatted expenses
    formatted_expenses = []
    if os.path.getsize("expenses.csv") == 0:
        print("No logged expenses! Add some!")
    else:
        print("YOUR EXPENSES")
        for i in range(len(expense)):
            if len(str(amount[i])[str(amount[i]).index(".")+1:]) == 1 and str(amount[i])[str(amount[i]).index(".")+1:] == "0":
                formatted_expenses.append(f"{i+1}. {expense[i]} - ${amount[i]:.2f}")
            elif len(str(amount[i])[str(amount[i]).index(".")+1:]) == 1:
                formatted_expenses.append(f"{i+1}. {expense[i]} - ${amount[i]:.2f}")
            elif len(str(amount[i])[str(amount[i]).index(".")+1:]) == 2:
                formatted_expenses.append(f"{i+1}. {expense[i]} - ${amount[i]}")

    # Holds numbers to run against user choice
    num_list = []
    for i in range(len(formatted_expenses)):
        num_list.append(formatted_expenses[i][0])

    # Prints full add expense menu
    print("0. Add new expense")
    for i in formatted_expenses:
        print(i)

    # Adds/updates expenses
    while True:
        exp_choice_int = input("Choose a number or \"back\": ")
        try:
            if exp_choice_int in num_list:
                for i in range(len(expense)):
                    if exp_choice_int == num_list[i]:
                        ex_amount = float(input("Enter the price of your expense: "))
                        for i in range(len(expense)):
                            if exp_choice_int == num_list[i]:
                                amount[i] = amount[i] + ex_amount
                open("expenses.csv", "w").close()
                for i in range(len(expense)):
                    with open("expenses.csv", "a", newline="") as x:
                        expenses_file = csv.writer(x)
                        expenses_file.writerow([expense[i], amount[i]])
                clear_screen()
                print(f"Expense amount updated!")
                break
            elif exp_choice_int == "0":
                my_expense = input("Describe your expense: ")
                ex_amount = float(input("Enter price of your expense: "))
                with open("expenses.csv", "a", newline="") as x:
                    expenses_file = csv.writer(x)
                    expenses_file.writerow([my_expense, ex_amount])
                clear_screen()
                print(f"Expense and amount added to expense list!")
                break
            elif exp_choice_int.lower() == "back":
                clear_screen()
                break
            else:
                clear_screen()
                print("Error: Invalid selection")
                pass
        except ValueError:
            clear_screen()
            print("Enter a number or \"back\"")
            pass

# Lists all expenses
def view_expenses():
    with open("expenses.csv") as x:
        expenses_file = csv.reader(x, delimiter=',')
        expense = []
        amount = []
        for i in expenses_file:
            expense.append(i[0])
            amount.append(i[1])
    for i in range(len(expense)):
        if len(str(amount[i])[str(amount[i]).index(".")+1:]) == 1 and str(amount[i])[str(amount[i]).index(".")+1:] == "0":
            print(f"{i+1}. {expense[i]} - ${amount[i]:.2f}")
            break
        elif len(str(amount[i])[str(amount[i]).index(".")+1:]) == 1:
            print(f"{i+1}. {expense[i]} - ${amount[i]:.2f}")
            break
        elif len(str(amount[i])[str(amount[i]).index(".")+1:]) == 2:
            print(f"{i+1}. {expense[i]} - ${amount[i]}")
            break

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
            '''elif int_choice == 3:
                clear_screen()
                calculate_expenses()
            else:
                clear_screen()
                print("Choice not found...")
                pass'''
        except ValueError:
            clear_screen()
            print("Choice not found...")
            pass

'''
def view_expenses():
    if len(expenses) == 0:
        print("There are no expenses in your tracker! Add some by pressing 1")
    else:
        for key,value in expenses.items():
            if len(str(value)[str(value).index(".")+1:]) == 1 and str(value)[str(value).index(".")+1:] == "0":
                print(f"{key}: ${int(value)}")
            elif len(str(value)[str(value).index(".")+1:]) == 1:
                print(f"{key}: ${value:.2f}")
            elif len(str(value)[str(value).index(".")+1:]) == 2:
                print(f"{key}: ${value}")
            else:                
                print(f"{key}: ${int(value)}")

def calculate_expenses():
    total = 0
    if len(expenses) == 0:
        print("There are no expenses in your tracker! Add some by pressing 1")
    else:
        for expense in expenses.values():
            total += expense

        if len(str(total)[str(total).index(".")+1:]) == 1 and str(total)[str(total).index(".")+1:] == "0":
            print(f"The total of your expenses comes out to: ${int(total)}")
        elif len(str(total)[str(total).index(".")+1:]) == 1:
            print(f"The total of your expenses comes out to: ${total:.2f}")
        elif len(str(total)[str(total).index(".")+1:]) == 2:
            print(f"The total of your expenses comes out to: ${total}")
        else:
            print(f"The total of your expenses comes out to: ${int(total)}")
'''