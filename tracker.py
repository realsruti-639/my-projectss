import csv
import os

class ExpenseTracker:
    def __init__(self, filename="d:/my-projects/expenses.csv"):
        self.filename = filename
        # Ensure the directory exists on D drive
        os.makedirs(os.path.dirname(self.filename), exist_ok=True)
        # Create the CSV file with headers if it doesn't exist
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Category", "Amount", "Description"])

    def add_expense(self, date, category, amount, description):
        """Appends a new expense record directly to the D drive CSV file."""
        with open(self.filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount, description])
        print(f"\n✅ Successfully saved: ${amount:.2f} under '{category}'!")

    def view_expenses(self):
        """Reads and displays all recorded expenses in a clean list."""
        if not os.path.exists(self.filename) or os.path.getsize(self.filename) <= 40:
            print("\n📭 No expenses recorded yet.")
            return
        
        print("\n==================== CURRENT EXPENSE LOG ====================")
        with open(self.filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader) # Skip header row
            for row in reader:
                print(f"📅 {row[0]} | 🗂️ {row[1]:<13} | 💰 ${float(row[2]):<8.2f} | 📝 {row[3]}")
        print("=============================================================\n")

    def generate_summary(self):
        """Calculates budget metrics and prints a clean text-based analysis breakdown."""
        if not os.path.exists(self.filename) or os.path.getsize(self.filename) <= 40:
            print("\n❌ No data available to generate a summary report.")
            return

        category_totals = {}
        total_spending = 0.0
        
        with open(self.filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                category = row[1]
                amount = float(row[2])
                category_totals[category] = category_totals.get(category, 0.0) + amount
                total_spending += amount

        print("\n📊 ================= FINANCE SUMMARY REPORT =================")
        print(f"Total Combined Spending: ${total_spending:.2f}")
        print("-------------------------------------------------------------")
        for category, total in category_totals.items():
            percentage = (total / total_spending) * 100
            # Creates a text-based progress bar for visual tracking
            bar_length = int(percentage // 10)
            progress_bar = "■" * bar_length + "□" * (10 - bar_length)
            print(f"🗂️ {category:<12} : ${total:<8.2f} [{progress_bar}] {percentage:.1f}%")
        print("=============================================================\n")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("=== Personal Finance Tracker ===")
        print("1. Add New Expense")
        print("2. View Expense Log")
        print("3. View Finance Summary Report")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            date = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
            if not date:
                from datetime import date as dt
                date = dt.today().strftime("%Y-%m-%d")
            
            print("Categories: Food, Rent, Entertainment, Shopping, Bills, Other")
            category = input("Enter category: ").strip().capitalize()
            if not category:
                category = "Other"
            
            try:
                amount = float(input("Enter amount ($): ").strip())
            except ValueError:
                print("❌ Invalid amount. Please enter a valid number.")
                continue
                
            description = input("Enter short description: ").strip()
            if not description:
                description = "None"
                
            tracker.add_expense(date, category, amount, description)
            
        elif choice == "2":
            tracker.view_expenses()
            
        elif choice == "3":
            tracker.generate_summary()
            
        elif choice == "4":
            print("\n👋 Goodbye! Happy budgeting!")
            break
        else:
            print("❌ Invalid selection. Please choose a number from 1 to 4.\n")

if __name__ == "__main__":
    main()
