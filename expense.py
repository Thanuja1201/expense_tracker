class Expense:
    def __init__(self, amount, category, description, date):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = date

    def to_dict(self):
        return {
            "amount": self.amount,
            "category": self.category,
            "description": self.description,
            "date": self.date
        }

    def __str__(self):
        return (
            f"Amount      : ₹{self.amount}\n"
            f"Category    : {self.category}\n"
            f"Description : {self.description}\n"
            f"Date        : {self.date}"
        )