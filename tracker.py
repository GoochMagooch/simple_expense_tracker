import os
import csv

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("1. Add an expenses")
    print("2. View expensess")
    print("3. Calculate Total expensess")
    print("\"Menu\" to bring up menu")
    print("\"Exit\" to exit\n")

# Adds/updates expensess in expenses.csv
def add_expenses():
    # Separates expensess file into expenses and amounts
    with open("expenses.csv") as x:
        expenses_file = csv.reader(x, delimiter=',')
        expenses = []
        amounts = []
        for i in expenses_file:
            expenses.append(i[0])
            amounts.append(float(i[1]))

    # Defines list of formatted expensess
    formatted_expenses = []
    if os.path.getsize("expenses.csv") == 0:
        print("No logged expensess! Add some!")
    else:
        print("YOUR EXPENSES")
        for i in range(len(expenses)):
            if len(str(amounts[i])[str(amounts[i]).index(".")+1:]) == 1 and str(amounts[i])[str(amounts[i]).index(".")+1:] == "0":
                formatted_expenses.append(f"{i+1}. {expenses[i]} - ${amounts[i]:.2f}")
            elif len(str(amounts[i])[str(amounts[i]).index(".")+1:]) == 1:
                formatted_expenses.append(f"{i+1}. {expenses[i]} - ${amounts[i]:.2f}")
            elif len(str(amounts[i])[str(amounts[i]).index(".")+1:]) == 2:
                formatted_expenses.append(f"{i+1}. {expenses[i]} - ${amounts[i]}")

    # Holds numbers to run against user choice
    num_list = []
    for i in range(len(formatted_expenses)):
        num_list.append(int(formatted_expenses[i][0]))

    # Prints full add expenses menu
    print("0. Add new expenses")
    for i in formatted_expenses:
        print(i)

    # Adds/updates expensess
    while True:
        clear_screen()
        print("0. Add new expenses")
        for i in formatted_expenses:
            print(i)
        exp_choice_int = input("Choose a number or \"back\": ")
        if exp_choice_int.lower() == "back":
            clear_screen()
            break
        elif exp_choice_int == "0":
            my_expenses = input("Describe your expense or enter \"back\": ")
            if my_expenses.lower() == "back":
                pass
            else:
                ex_amount = input("Enter expense amount or enter \"back\": ")
                if ex_amount.lower() == "back":
                    pass
                else:
                    with open("expenses.csv", "a", newline="") as x:
                        expenses_file = csv.writer(x)
                        expenses_file.writerow([my_expenses, float(ex_amount)])
                    clear_screen()
                    print(f"Expense added!")
                    break
        else:
            try:
                int_choice = int(exp_choice_int)
                # add conditional for "back"
                if int_choice in num_list:
                    ex_amount = float(input("Enter the price of your expenses: "))
                    for i in range(len(expenses)):
                        if int_choice == num_list[i]:
                            amounts[i] = amounts[i] + ex_amount
                    open("expenses.csv", "w").close()
                    for i in range(len(expenses)):
                        with open("expenses.csv", "a", newline="") as x:
                            expenses_file = csv.writer(x)
                            expenses_file.writerow([expenses[i], amounts[i]])
                    clear_screen()
                    print(f"Expense updated!")
                    break
                else:
                    clear_screen()
                    print("Enter a number or \"back\"")
                    pass
            except ValueError:
                clear_screen()
                print("Enter a number or \"back\"")
                pass

# Lists all expensess
def view_expenses():
    with open("expenses.csv") as x:
        expenses_file = csv.reader(x, delimiter=',')
        expenses = []
        amounts = []
        for i in expenses_file:
            expenses.append(i[0])
            amounts.append(float(i[1]))
    
    if os.path.getsize("expenses.csv") == 0:
        clear_screen()
        print("No logged expenses! Add some by choosing option 1!\n")
    else:
        for i in range(len(expenses)):
            if len(str(amounts[i])[str(amounts[i]).index(".")+1:]) == 1 and str(amounts[i])[str(amounts[i]).index(".")+1:] == "0":
                print(f"{i+1}. {expenses[i]} - ${amounts[i]:.2f}")
            elif len(str(amounts[i])[str(amounts[i]).index(".")+1:]) == 1:
                print(f"{i+1}. {expenses[i]} - ${amounts[i]:.2f}")
            else:
                print(f"{i+1}. {expenses[i]} - ${amounts[i]}")

def calculate_expenses():
    total = 0
    # Separates expensess file into expenses and amounts
    with open("expenses.csv") as x:
        expenses_file = csv.reader(x, delimiter=',')
        amounts = []
        for i in expenses_file:
            amounts.append(float(i[1]))

    if os.path.getsize("expenses.csv") == 0:
        clear_screen()
        print("No logged expenses! Add some by choosing option 1!\n")
    else:
        for amount in amounts:
            total += amount

        if len(str(total)[str(total).index(".")+1:]) == 1 and str(total)[str(total).index(".")+1:] == "0":
            print(f"The total of your expensess comes out to: ${int(total)}")
        elif len(str(total)[str(total).index(".")+1:]) == 1:
            print(f"The total of your expensess comes out to: ${total:.2f}")
        else:
            print(f"The total of your expensess comes out to: ${total}")

def exit_program():
    print("Exiting expenses Tracker...Goodbye")
    exit()

print("Welcome to the Simple expenses Tracker\n")

while True:
    display_menu()

    choice = input("Please choose an option (1 - 3), \"menu\", or \"exit\": ")

    if choice.lower() == "exit":
        print("Are you sure you want to exit?")
        exit_choice = input("Press \"Y\" or \"N\": ")
        if exit_choice.lower() == "y":
            clear_screen()
            exit_program()
        else:
            clear_screen()
            pass
    elif choice.lower() == "menu":
        clear_screen()
    else:
        try:
            int_choice = int(choice)
            if int_choice == 1:
                clear_screen()
                add_expenses()
            elif int_choice == 2:
                clear_screen()
                view_expenses()
            elif int_choice == 3:
                clear_screen()
                calculate_expenses()
            else:
                clear_screen()
                print("Choice not found...")
                pass
        except ValueError:
            clear_screen()
            print("Choice not found...")
            pass