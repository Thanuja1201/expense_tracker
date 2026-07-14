from datetime import datetime
from expense import Expense
from expense_manager import ExpenseManager


manager = ExpenseManager()

while True:

    print("\n===== Personal Expense Tracker =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        try:
            amount = float(input("Enter amount: "))
        except ValueError:
            print("Amount must be numeric.")
            continue

        category = input("Enter category: ")
        description = input("Enter description: ")

        date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")

        if date == "":
            date = datetime.today().strftime("%Y-%m-%d")

        expense = Expense(amount, category, description, date)

        manager.add_expense(expense)

        print("Expense added successfully.")

    elif choice == "2":

        manager.view_expenses()

    elif choice == "3":

        manager.view_expenses()

        try:
            number = int(input("Enter expense number to delete: "))
            manager.delete_expense(number)
        except ValueError:
            print("Please enter a valid number.")

    elif choice == "4":

        print("Thank you for using Expense Tracker.")
        break

    else:

        print("Invalid choice.")