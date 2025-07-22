import json
from datetime import datetime


class Transaction:
    def __init__(self, t_type, amount, category, date=None):
        self.t_type = t_type
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.now().strftime("%Y-%m-%d")

    def to_tuple(self):
        return (self.t_type, self.amount, self.category, self.date)

    def __str__(self):
        return f"{self.date} - {self.t_type.title()}: ${self.amount} ({self.category})"


class FinanceTracker:
    def __init__(self):
        self.transactions = []
        self.load_transactions_from_file()

    def load_transactions_from_file(self):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                for t in data:
                    transaction = Transaction(
                        t['type'], t['amount'], t['category'], t['date'])
                    self.transactions.append(transaction)
        except FileNotFoundError:
            pass

    def save_transactions_to_file(self):
        with open("data.json", "w") as file:
            json.dump([t.__dict__ for t in self.transactions], file, indent=4)

    def add_transaction(self, t_type, amount, category):
        transaction = Transaction(t_type, amount, category)
        self.transactions.append(transaction)
        self.save_transactions_to_file()

    def view_transactions(self):
        if not self.transactions:
            print("No transactions yet.")
            return
        print("\n📋 All Transactions:")
        for t in self.transactions:
            print(t)

    def calculate_balance(self):
        income = sum(
            t.amount for t in self.transactions if t.t_type == 'income')
        expenses = sum(
            t.amount for t in self.transactions if t.t_type == 'expense')
        balance = income - expenses
        print(f"\n📊 Monthly Summary:")
        print(f"Total Income: ${income}")
        print(f"Total Expenses: ${expenses}")
        print(f"Balance: ${balance}\n")

    def filter_by_category(self, category):
        filtered = [t for t in self.transactions if t.category == category]
        if not filtered:
            print(f"No transactions found for category '{category}'.")
            return
        for t in filtered:
            print(t)

    def export_summary_to_csv(self):
        with open("monthly_summary.csv", "w") as file:
            file.write("Date,Type,Amount,Category\n")
            for t in self.transactions:
                file.write(f"{t.date},{t.t_type},{t.amount},{t.category}\n")
        print(" Summary exported to 'monthly_summary.csv'.")
