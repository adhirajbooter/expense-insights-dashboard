import csv
import matplotlib.pyplot as plt

FILENAME = "expenses.csv"
CHART_FILENAME = "expense_pie_chart.png"


def load_expenses(filename):
    expenses = []
    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    amount = float(row["amount"])
                except ValueError:
                    continue

                expenses.append({
                    "date": row["date"],
                    "description": row["description"],
                    "category": row["category"],
                    "amount": amount
                })
    except FileNotFoundError:
        print(f"❌ Could not find file: {filename}")
        return []

    return expenses


def analyze_expenses(expenses):
    total_spent = 0.0
    category_totals = {}

    for expense in expenses:
        amount = expense["amount"]
        category = expense["category"]

        total_spent += amount

        if category not in category_totals:
            category_totals[category] = 0.0
        category_totals[category] += amount

    return total_spent, category_totals


def generate_pie_chart(category_totals):
    labels = category_totals.keys()
    sizes = category_totals.values()

    plt.figure(figsize=(8, 8))
    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=140
    )
    plt.title("Spending by Category")

    plt.savefig(CHART_FILENAME)
    plt.close()

    print(f"\n📊 Chart saved as '{CHART_FILENAME}'")


def print_report(total_spent, category_totals):
    print("===== Personal Expense Report =====\n")

    print(f"Total spent: ${total_spent:.2f}\n")

    print("Spending by category:")
    for category, total in category_totals.items():
        print(f" - {category}: ${total:.2f}")


def main():
    expenses = load_expenses(FILENAME)
    if not expenses:
        print("No valid expenses to analyze.")
        return

    total_spent, category_totals = analyze_expenses(expenses)

    print_report(total_spent, category_totals)

    generate_pie_chart(category_totals)


if __name__ == "__main__":
    main()
