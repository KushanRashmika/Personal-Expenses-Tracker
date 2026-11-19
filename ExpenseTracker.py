from datetime import date

from ExpenseLog import ExpenseLog
from Budget import Budget
from Expense import Expense
from Functions import parse_amount, format_money, is_same_month

class ExpenseTracker:
    def __init__(self):
        self.log = ExpenseLog()
        self.budgets = {}

    def set_budget(self, category, limit):
        self.budgets[category] = Budget(category, limit)

    def record(self, amount_text, category, description):
        expense = Expense(parse_amount(amount_text), category, description, date.today())
        self.log.add_expense(expense)
        return f"Expense recorded: {expense}"

    def budget_status(self, category):
        try:
            total_spent = self.log.total_by_category(category)
        except KeyError:
            return f"No budget set for category: {category}"
        
        budget = self.budgets[category]
        remaining = budget.remaining(total_spent)

        if budget.is_exceeded(total_spent):
            return {"spent": format_money(total_spent), "limit": format_money(budget.limit), "remaining": format_money(-remaining), "Exceeded": True}
        else:
            return {"spent": format_money(total_spent), "limit": format_money(budget.limit), "remaining": format_money(remaining), "Exceeded": False}


    def monthly_report(self, month: int, year: int) -> str:
        report = f"\nMonthly Report for {month}/{year}\n\n"
        monthly_expenses = self.log.filter_by_month(month, year)
        category_totals = {}

        for expense in monthly_expenses:
            if expense.category not in category_totals:
                category_totals[expense.category] = 0.0
            category_totals[expense.category] += expense.amount

        for category, total in category_totals.items():
            report += f"Category: {category}\nTotal Spent: {format_money(total)}\n"

        report += f"\nTotal Expenses: {format_money(sum(expense.amount for expense in monthly_expenses))}\n"

        return report