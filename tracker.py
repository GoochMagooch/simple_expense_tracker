import os
import csv

# START DATE: AUGUST 18, 2024
# COMPLETION DATE: MAY 21, 2025
# HAPPY CODING! :)

# FUNCTION 1: CLEARS THE TERMINAL
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# FUNCTION 2: DISPLAYS MAIN CLI INTERFACE MENU
def display_menu():
    print("Welcome to the Simple expenses Tracker\n")
    print("1. Manage Expenses")
    print("2. View Expenses")
    print("3. Calculate Total Expenses")
    print("\"Menu\" to display menu")
    print("\"Exit\" to exit\n")

# FUNCTION 3: ADDS/UPDATES/REMOVES EXPENSES
def add_expenses():
    clear_screen()
    # Adds/updates expenses
    while True:

        # Separates expenses file into expenses and amounts
        with open("expenses.csv") as x:
            expenses_file = csv.reader(x, delimiter=',')
            expenses = []
            amounts = []
            for i in expenses_file:
                expenses.append(i[0].lower())
                amounts.append(float(i[1]))

        # Defines list of formatted expenses
        formatted_expenses = []
        for i in range(len(expenses)):
            if len(str(amounts[i])[str(amounts[i]).index(".")+1:]) == 1 and str(amounts[i])[str(amounts[i]).index(".")+1:] == "0":
                formatted_expenses.append(f"{i+1}. {expenses[i]} - ${amounts[i]:.2f}")
            elif len(str(amounts[i])[str(amounts[i]).index(".")+1:]) == 1:
                formatted_expenses.append(f"{i+1}. {expenses[i]} - ${amounts[i]:.2f}")
            elif len(str(amounts[i])[str(amounts[i]).index(".")+1:]) == 2:
                formatted_expenses.append(f"{i+1}. {expenses[i]} - ${amounts[i]}")

        # Stores numbers to match with corresponding user expense number
        num_list = []
        for i in range(len(formatted_expenses)):
            num_list.append(int(formatted_expenses[i][0]))

        # Main 'Expense Management Console' Menu
        print("Welcome to the Expense Management Console!\n")
        if len(expenses) == 0:
            print("No logged expenses! Add some by entering \"Add\"!")
        else:
            print("Enter \"Add\" to add new expense")
            if len(expenses) == 1:
                print(f"Choose 1 to update expense amount")
                for i in formatted_expenses:
                    print(f"  {i}")
            else:
                print(f"Choose 1 - {len(expenses)} to update expense amount")
                for i in formatted_expenses:
                    print(f"  {i}")
        print("Enter \"Remove\" to remove expense")
        print("Enter \"Back\" to go back")
        
        exp_choice_int = input("Choose: ")

        # If user chooses "back"
        if exp_choice_int.lower() == "back":
            clear_screen()
            break

        # If user chooses "add"
        elif exp_choice_int.lower() == "add":
            while True:
                # If there are no logged expenses
                if len(expenses) == 0:
                    clear_screen()
                    print("ADD YOUR FIRST EXPENSE!\n")

                # If there is one logged expense
                elif len(expenses) == 1:
                    clear_screen()
                    print("ADD NEW EXPENSES HERE!\n")
                    print(f"Choose 1 to update expense amount")
                    for i in formatted_expenses:
                        print(f"  {i}")

                # If there are multiple logged expenses
                else:
                    clear_screen()
                    print("ADD NEW EXPENSES HERE!\n")
                    print(f"Current Expenses:")
                    for i in formatted_expenses:
                        print(f"  {i}")
                    print("Enter \"Remove\" to remove expense")
                    print("Enter \"Back\" to go back")
                my_expenses = input("Enter your expense: ")
                if my_expenses.lower() in expenses:
                    clear_screen()
                    print("This expense already exists\n")
                    break
                elif my_expenses.lower() == "back":
                    clear_screen()
                    break
                else:
                    ex_amount = input("Enter amount: ")
                    if ex_amount.lower() == "back":
                            clear_screen()
                            pass
                    else:
                        try:
                            ex_amount_float = float(ex_amount)
                            with open("expenses.csv", "a", newline="") as x:
                                expenses_file = csv.writer(x)
                                expenses_file.writerow([my_expenses, ex_amount_float])
                            clear_screen()
                            print(f"Expense added!")
                            break
                        except ValueError:
                            print("test")

        # If user chooses "remove"
        elif exp_choice_int.lower() == "remove":
            while True:
                # If there are no logged expenses
                if len(expenses) == 0:
                    clear_screen()
                    print("No expenses to remove! Add some!\n")
                    break

                # If there is one logged expense
                elif len(expenses) == 1:
                    clear_screen()
                    print("REMOVE EXPENSES HERE!\n")
                    print(f"Choose 1 to remove expense")
                    for i in formatted_expenses:
                        print(f"  {i}")

                # If there are multiple logged expenses
                else:
                    clear_screen()
                    print("REMOVE EXPENSES HERE!\n")
                    print(f"Current Expenses:")
                    for i in formatted_expenses:
                        print(f"  {i}")
                    print("Enter \"Back\" to go back")
                remove_exp = input("Expense to remove: ")
                if remove_exp.lower() == "back":
                    clear_screen()
                    break
                else:
                    try:
                        remove_conf_int = int(remove_exp)
                        if remove_conf_int in num_list:
                            print("Are you sure you want to remove this expense?")
                            confirm_removal = input("Enter \"Y\" or \"N\": ")
                            if confirm_removal.lower() == "y":
                                    # Remove Expense Logic
                                    clear_screen()
                                    exp_ph = ""
                                    amo_ph = ""
                                    for i in range(len(formatted_expenses)):
                                        if remove_conf_int == int(formatted_expenses[i][0]):
                                            exp_ph = expenses[i]
                                            amo_ph = amounts[i]
                                    expenses.remove(exp_ph)
                                    amounts.remove(amo_ph)
                                    open("expenses.csv", "w").close()
                                    for i in range(len(expenses)):
                                        with open("expenses.csv", "a", newline="") as x:
                                            expenses_file = csv.writer(x)
                                            expenses_file.writerow([expenses[i], amounts[i]])
                                    break
                            else:
                                clear_screen()
                                break
                        else:
                            print("Invalid selection")
                            pass
                    except ValueError:
                        pass
                        print("test")      
        else:
            try:
                int_choice = int(exp_choice_int)
                if int_choice in num_list:
                    clear_screen()
                    print("Welcome to the Expense Management Console!\n")
                    print("Enter \"Add\" to add new expense")
                    if len(expenses) == 1:
                        print(f"Choose 1 to update expense amount")
                        for i in formatted_expenses:
                            print(f"  {i}")
                    else:
                        print(f"Choose 1 - {len(expenses)} to update expense amount")
                        for i in formatted_expenses:
                            print(f"  {i}")
                    print("Enter \"Remove\" to remove an expense")
                    print("Enter \"Back\" to go back")
                    for i in range(len(num_list)):
                        if num_list[i] == int_choice:
                            ex_amount = float(input(f"Enter the price of your {expenses[i]} expense: "))
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
                    print("Enter a valid expense number or \"back\"")
                    pass
            except ValueError:
                clear_screen()
                print("Enter a number or \"back\"")
                pass

# FUNCTION 4: OUTPUTS ALL LOGGED EXPENSES
def view_expenses():
    if os.path.getsize("expenses.csv") == 0:
        clear_screen()
        print("No logged expenses! Add some!\n")
        pass
    else:
        with open("expenses.csv") as x:
            expenses_file = csv.reader(x, delimiter=',')
            expenses = []
            amounts = []
            for i in expenses_file:
                expenses.append(i[0])
                amounts.append(float(i[1]))

            for i in range(len(expenses)):
                if len(str(amounts[i])[str(amounts[i]).index(".")+1:]) == 1 and str(amounts[i])[str(amounts[i]).index(".")+1:] == "0":
                    print(f"{i+1}. {expenses[i]} - ${amounts[i]:.2f}")
                elif len(str(amounts[i])[str(amounts[i]).index(".")+1:]) == 1:
                    print(f"{i+1}. {expenses[i]} - ${amounts[i]:.2f}")
                else:
                    print(f"{i+1}. {expenses[i]} - ${amounts[i]}")

# FUNCTION 5: CALCULATES/OUTPUTS SUM OF EXPENSES
def calculate_expenses():
    total = 0
    # Separates expenses file into expenses and amounts
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

# CLI USER INTERFACE LOOP
while True:
    display_menu()
    choice = input("Please choose an option (1 - 3), \"menu\", or \"exit\": ")

    if choice.lower() == "exit":
        clear_screen()
        print("Exiting expenses Tracker...Goodbye")
        exit()
    elif choice.lower() == "menu":
        clear_screen()
        display_menu()
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
