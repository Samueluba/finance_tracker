def validate_amount(amount):
    """Ensure the amount is a positive number."""
    try:
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be positive.")
        return amount
    except ValueError as e:
        print(f" Invalid amount: {e}")
        return None


def validate_transaction_type(t_type):
    """Ensure the transaction type is either 'income' or 'expense'."""
    if t_type not in ["income", "expense"]:
        print(" Invalid transaction type. Must be 'income' or 'expense'.")
        return False
    return True
