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


def show_summary(purchases, starting_budget):
    total_spent = sum(p["cost"] for p in purchases)
    remaining = starting_budget - total_spent

    print("\n Spending Summary ")
    print(f"Total Spent: {format_currency(total_spent)}")
    print(f"Remaining Budget: {format_currency(remaining)}")

    print("\nSpending by Category:")
    categories = {}
    for p in purchases:
        categories[p["category"]] = categories.get(p["category"], 0) + p["cost"]

    for category, amount in categories.items():
        print(f" - {category}: {format_currency(amount)}")

    return remaining

def show_spending_log(purchases):
    print("\n Itemized Spending Log ")
    if not purchases:
        print("No purchases recorded yet.")
        return

    for p in purchases:
        print(f"- {p['item']} : {format_currency(p['cost'])} ({p['category']})")

    total = sum(p["cost"] for p in purchases)
    print(f"\nTotal Spent: {format_currency(total)}")

def fashion_recommendations(remaining):
    print("\n AI Fashion Recommendations ")

    if remaining < 20:
        print("Your budget is very low. Try:")
        print("- Thrift stores")
        print("- Clearance racks")
    elif remaining < 50:
        print("Affordable options:")
        print("- Basic tees from H&M or Target")
        print("- Casual shoes on sale")
    elif remaining < 100:
        print("You can upgrade your style:")
        print("- Quality sneakers")
        print("- Stylish hoodies")
    else:
        print("You have great flexibility! Consider:")
        print("- Premium clothing pieces")
        print("- Branded shoes")
        print("- Quality accessories")

    print(f"\nRemaining Budget: {format_currency(remaining)}")


def ai_recommendation(remaining):
    if remaining < 20:
        return "⚠️ Warning: Your budget is almost gone. Avoid extra spending!"
    elif remaining < 50:
        return "Be careful — your budget is getting low."
    else:
        return "You're managing your budget well!"

def main():
    print("Welcome to StyleSaver\n")
    purchases = []

    budget = set_monthly_budget()
    starting_budget = budget
    print(f"Budget stored in main: {format_currency(budget)}\n")

    while True:
        add_more = input("Do you want to add a purchase? (y/n): ").lower()
        if add_more != 'y':
            break

        purchase = add_purchase()
        purchases.append(purchase)

        budget = update_remaining_budget(budget, purchase["cost"])
        print()

    final_remaining = show_summary(purchases, starting_budget)

   
    show_spending_log(purchases)
    fashion_recommendations(final_remaining)

    print("\nAI Recommendation:", ai_recommendation(final_remaining))

    print("\nThank you for using StyleSaver!")

if __name__ == "__main__":
    main()
