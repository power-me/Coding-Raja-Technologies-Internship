transactions = []

def add_transaction(category, amount):
    transaction = {'category': category, 'amount': amount}
    transactions.append(transaction)

def calculate_budget():
    total_income = sum(transaction['amount'] for transaction in transactions if transaction['category'] == 'income')
    total_expenses = sum(transaction['amount'] for transaction in transactions if transaction['category'] == 'expense')
    remaining_budget = total_income - total_expenses
    return remaining_budget

def analyze_expenses():
    expense_categories = set(transaction['category'] for transaction in transactions if transaction['category'] != 'income')
    expense_totals = {category: sum(transaction['amount'] for transaction in transactions if transaction['category'] == category) for category in expense_categories}
    return expense_totals

# Prompt the user for input and perform the necessary operations

while True:
    print("1. Add transaction")
    print("2. Calculate budget")
    print("3. Analyze expenses")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        category = input("Enter category (income/expense): ")
        amount = float(input("Enter amount: "))
        add_transaction(category, amount)
    elif choice == '2':
        remaining_budget = calculate_budget()
        print("Remaining budget: $", remaining_budget)
    elif choice == '3':
        expense_totals = analyze_expenses()
        for category, total in expense_totals.items():
            print(category, ":", total)
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")
