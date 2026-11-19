class ExpenseLog:
    def __init__(self):
        self.expenses = []
    
    def add_expense(self, expense):
        self.expenses.append(expense)

    def total(self):
        total = 0.0
        for expense in self.expenses:
            total += expense.amount
        return total

    def total_by_category(self, category):
        total = 0.0
        for expense in self.expenses:
            if category == expense.category:
                total += expense.amount
        return total

    def filter_by_month(self, month: int, year: int):
        filtered_expenses = []
        for expense in self.expenses:
            expense_date = expense.date
            if expense_date.month == month and expense_date.year == year:
                filtered_expenses.append(expense)
        return filtered_expenses
    