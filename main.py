from ExpenseTracker import ExpenseTracker

class ExpenseTrackerApp:
    def __init__(self):
        self.tracker = ExpenseTracker()

    def run(self):
        while True:
            print("\nExpense Tracker Menu:")
            print("1. Set Budget")
            print("2. Record Expense")
            print("3. Check Budget Status")
            print("4. Generate Monthly Report")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                category = input("Enter category: ")
                limit = float(input("Enter budget limit: "))
                self.tracker.set_budget(category, limit)
                print(f"Budget set for {category} with limit {limit}")

            elif choice == '2':
                amount_text = input("Enter expense amount: ")
                category = input("Enter category: ")
                description = input("Enter description: ")
                result = self.tracker.record(amount_text, category, description)
                print(result)

            elif choice == '3':
                category = input("Enter category to check budget status: ")
                status = self.tracker.budget_status(category)
                if isinstance(status, dict):
                    print(f"Spent: {status['spent']}, Limit: {status['limit']}, Remaining: {status['remaining']}, Exceeded: {status['Exceeded']}")
                else:
                    print(status)

            elif choice == '4':
                month = int(input("Enter month (1-12): "))
                year = int(input("Enter year (e.g., 2024): "))
                report = self.tracker.monthly_report(month, year)
                print(report)

            elif choice == '5':
                print("Exiting Expense Tracker.")
                break

            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = ExpenseTrackerApp()
    app.run()