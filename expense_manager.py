import json
import os
from expense import Expense


class ExpenseManager:
    def __init__(self, filename="expenses.json"):
        self.filename = filename
        self.expenses = []
        self.load_expenses()

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        if not self.expenses:
            print("\nNo expenses found.\n")
            return

        print("\n===== Expenses =====\n")

        for index, expense in enumerate(self.expenses, start=1):
            print(f"Expense #{index}")
            print(expense)
            print("-" * 30)

    def delete_expense(self, index):
        try:
            deleted = self.expenses.pop(index - 1)
            self.save_expenses()
            print(f"\nDeleted: {deleted.description}\n")
        except IndexError:
            print("\nInvalid expense number.\n")

    def save_expenses(self):
        data = []

        for expense in self.expenses:
            data.append(expense.to_dict())

        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_expenses(self):
        if not os.path.exists(self.filename):
            return

        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

            for item in data:
                expense = Expense(
                    item["amount"],
                    item["category"],
                    item["description"],
                    item["date"]
                )
                self.expenses.append(expense)

        except json.JSONDecodeError:
            print("JSON file is empty or corrupted.")