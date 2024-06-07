import json
import os

# Define the file to store transactions
DATA_FILE = 'finances.json'

# Load transactions from file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            return json.load(file)
    return {'income': [], 'expenses': []}

# Save transactions to file
def save_data(data):
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Add a new income or expense
def add_transaction(data, transaction_type):
    description = input(f"Enter {transaction_type} description: ")
    amount = float(input(f"Enter {transaction_type} amount: "))
    data[transaction_type].append({"description": description, "amount": amount})
    save_data(data)
    print(f"{transaction_type.capitalize()} added successfully!")

# View a summary of finances
def view_summary(data):
    total_income = sum(item['amount'] for item in data['income'])
    total_expenses = sum(item['amount'] for item in data['expenses'])
    net_balance = total_income - total_expenses

    print("\nSummary:")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Net Balance: ${net_balance:.2f}")

# Main menu
def main():
    data = load_data()
    while True:
        print("\nPersonal Finance Tracker")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction(data, 'income')
        elif choice == '2':
            add_transaction(data, 'expenses')
        elif choice == '3':
            view_summary(data)
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
