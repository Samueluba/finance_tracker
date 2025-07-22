import sys
from tracker import FinanceTracker
from my_utils import validate_amount, validate_transaction_type


def main():
    tracker = FinanceTracker()

    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. View Balance")
        print("4. Filter by Category")
        print("5. Export Monthly Summary")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            t_type = input("Type (income/expense): ").lower()
            if not validate_transaction_type(t_type):
                continue

            amount = input("Enter amount: $")
            amount = validate_amount(amount)
            if amount is None:
                continue

            category = input("Enter category (e.g., food, salary): ")
            tracker.add_transaction(t_type, amount, category)
            print(" Transaction added!\n")

        elif choice == '2':
            tracker.view_transactions()

        elif choice == '3':
            tracker.calculate_balance()

        elif choice == '4':
            category = input("Enter category to filter by: ")
            tracker.filter_by_category(category)

        elif choice == '5':
            tracker.export_summary_to_csv()

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print(" Invalid choice. Try again.")


if __name__ == "__main__":
    main()
