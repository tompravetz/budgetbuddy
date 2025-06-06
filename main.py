import json
from colorama import init, Fore, Style
init(autoreset=True)

def show_menu():
    """Prints the menu options for the user."""
    print("\nMenu:")
    print("1. Add an income")
    print("2. Add an expense")
    print("3. View financial summary")
    print("4. Save and exit")

def add_income():
    """Adds an income to the user's account."""
    amount = float(input("Enter the amount of income: "))
    description = input("Enter a description for the income: ")
    entries.append({"type": "income", "amount": amount, "description": description})
    print("Income added successfully!")

def add_expense():
    """Adds an expense to the user's account."""
    amount = float(input("Enter the amount of expense: "))
    description = input("Enter a description for the expense: ")
    entries.append({"type": "expense", "amount": amount, "description": description})
    print("Expense added successfully!")

def view_summary():
    """Displays the user's financial summary."""
    print(f"\n{Fore.CYAN}=== Transaction History ==={Style.RESET_ALL}")
    for entry in entries:
        color = Fore.GREEN if entry['type'] == 'income' else Fore.RED
        type_label = entry['type'].capitalize()
        print(f"{color}{type_label:<8} | ${entry['amount']:>8.2f} | {entry['description']}{Style.RESET_ALL}")
    
    total_income = sum(entry["amount"] for entry in entries if entry["type"] == "income")
    total_expense = sum(entry["amount"] for entry in entries if entry["type"] == "expense")
    net = total_income - total_expense

    print(f"\n{Fore.CYAN}=== Financial Summary ==={Style.RESET_ALL}")
    print(f"{Fore.GREEN}Total Income:  ${total_income:.2f}{Style.RESET_ALL}")
    print(f"{Fore.RED}Total Expense: ${total_expense:.2f}{Style.RESET_ALL}")
    
    net_color = Fore.GREEN if net >= 0 else Fore.RED
    print(f"{net_color}Net Balance:   ${net:.2f}{Style.RESET_ALL}\n")

def save_and_exit():
    """Saves the user's data to data.json and exits."""
    with open("data.json", "w") as f:
        json.dump(entries, f, indent=2)
    print("Data saved. Exiting...")

def load_data():
    """Loads the user's data from data.json."""
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

entries = load_data()

print()
print("========================")
print(Style.BRIGHT +"Welcome to Budget Buddy!")
print("========================")

while True:
    show_menu()
    user_input = input("Please enter the number of the option you want to choose: ")
    match user_input:
        case"1":
            add_income()
        case "2":
            add_expense()
        case "3":
            view_summary()
        case "4":
            save_and_exit()
            break
        case _:
            print("Invalid input")