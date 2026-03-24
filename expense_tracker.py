import os

FILE_NAME = "expenses.txt"

def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category (Food/Travel/Other): ")
    amount = input("Enter amount: ")
    description = input("Enter description: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{category},{amount},{description}\n")

    print("✅ Expense added successfully!\n")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.\n")
        return

    print("\n--- Expense Records ---")
    with open(FILE_NAME, "r") as file:
        for line in file:
            date, category, amount, description = line.strip().split(",")
            print(f"Date: {date} | Category: {category} | Amount: ₹{amount} | Desc: {description}")
    print()


def total_expense():
    if not os.path.exists(FILE_NAME):
        print("No expenses found.\n")
        return

    total = 0
    with open(FILE_NAME, "r") as file:
        for line in file:
            amount = float(line.strip().split(",")[2])
            total += amount

    print(f"\n💰 Total Expense: ₹{total}\n")


def menu():
    while True:
        print("====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            total_expense()
        elif choice == '4':
            print("Exiting... 👋")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    menu()
