class Expense:
    def __init__(self, amount, category, description, date):
        if(amount > 0):
            self.amount = amount
        else:
            raise ValueError("Amount must be positive.")
        if category is not None:
            self.category = category
        else:
            raise ValueError("Category can't be empty.")
        self.description = description
        self.date = date

    def __str__(self):
        return f"{self.amount} has been expensed on {self.date}\nfor {self.description}\nCategory: {self.category}"