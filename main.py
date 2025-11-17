def format_currency(amount):
    """Return a number formatted as standard currency."""
    return f"${amount:.2f}"

def set_monthly_budget():
    while True:
        try:
            budget = float(input("Enter your monthly budget amount: $"))

            if budget < 0:
                print("Budget cannot be negative. Please enter a valid number.")
                continue

            print(f"Your monthly budget is set to: {format_currency(budget)}")
            return budget

        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    print("Welcome to StyleSaver")
    budget = set_monthly_budget()
    print(f"Budget stored in main: {format_currency(budget)}")

if __name__ == "__main__":
    main()
