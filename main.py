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

def add_purchase():
    item = input("Enter the item you purchased: ")
    while True:
        try:
            cost = float(input("Enter the cost of this item: $"))
            if cost < 0:
                print("Cost cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    category = input("Enter a category for this purchase: ")
    purchase = {"item": item, "cost": cost, "category": category}
    print(f"Purchase added: {item} - {format_currency(cost)} ({category})")
    return purchase

def update_remaining_budget(budget, purchase_cost):
    """Subtract purchase cost from remaining budget."""
    remaining = budget - purchase_cost
    print(f"Remaining budget: {format_currency(remaining)}")
    return remaining

def main():
    print("Welcome to StyleSaver\n")
    budget = set_monthly_budget()
    print(f"Budget stored in main: {format_currency(budget)}\n")

    
    while True:
        add_more = input("Do you want to add a purchase? (y/n): ").lower()
        if add_more != 'y':
            break

        purchase = add_purchase()
        budget = update_remaining_budget(budget, purchase["cost"])
        

    print(f"Final remaining budget: {format_currency(budget)}")
    print("Thank you for using StyleSaver!")

if __name__ == "__main__":
    main()
