"""
Personal Expense Tracker
A command-line application for tracking personal expenses with data persistence.

Features:
- Add expenses with categories and dates
- View all expenses with totals
- Group expenses by category
- Data persists between sessions using JSON
- Error handling for invalid input and file operations

Technologies Used:
- Python 3
- JSON for data storage
- datetime module for date tracking
- File I/O operations

Author: [Janai Pinnock]
Date: September 2025
"""

import json
from datetime import datetime 
def save_expenses(expenses):

    with open("expenses.json", "w") as file:
        json.dump(expenses, file)
        print("Expenses saved to expenses.json")

def load_expenses():
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

print("💰 Welcome to Your Personal Expense Tracker! 💰")
print("=" * 50)

#  store expenses in a list of dictionaries
# Each expense will have: amount, category, description, date
expenses = load_expenses()

# Main menu loop
while True:
    print("\nWhat would you like to do?")
    print("1. Add an expense")
    print("2. View all expenses") 
    print("3. View expenses by category")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ")
    
    #  Handle different menu choices with conditions
    if choice == "1":
        print("\n--- Adding New Expense ---")
        
        # Get expense details from user
        try:
            amount = float(input("Enter amount: $"))
            category = input("Enter category (Food, Transport, Entertainment, etc.): ")
            description = input("Enter description: ")
            
            # Create a dictionary to store this expense
            expense = {
                "amount": amount,
                "category": category.title(),  # Makes first letter uppercase
                "description": description,
                "date": datetime.now().strftime("%Y-%m-%d") 
            }

            # Add to our expenses list
            expenses.append(expense)
            save_expenses(expenses)
            print(f"✅ Added expense: ${amount:.2f} for {category}")
            
        except ValueError:
            print("❌ Please enter a valid amount!")
            
    elif choice == "2":
        print("\n--- All Your Expenses ---")
        
        if len(expenses) == 0:
            print("No expenses recorded yet!")
        else:
            total = 0
            print(f"{'Category':<15} {'Amount':<10} {'Description'}")
            print("-" * 45)
            
            # Loop through all expenses (like your guessing game loop!)
            for expense in expenses:
                amount = expense["amount"]
                category = expense["category"]
                description = expense["description"]
                date = expense.get("date", "No date")  

                print(f"{category:<15} ${amount:<9.2f} {description} on {date}")
                total += amount
            
            print("-" * 45)
            print(f"{'TOTAL':<15} ${total:<9.2f}")
            
    elif choice == "3":
        print("\n--- Expenses by Category ---")
        
        if len(expenses) == 0:
            print("No expenses recorded yet!")
        else:
            # Create a dictionary to group expenses by category
            categories = {}
            
            # Group expenses by category
            for expense in expenses:
                category = expense["category"]
                amount = expense["amount"]
                
                # If category doesn't exist in our dictionary, create it
                if category not in categories:
                    categories[category] = []
                
                # Add this expense to the category
                categories[category].append(expense)
            
            # Display each category
            for category, category_expenses in categories.items():
                print(f"\n📊 {category}:")
                category_total = 0
                
                for expense in category_expenses:
                    amount = expense["amount"]
                    description = expense["description"]
                    print(f"  ${amount:.2f} - {description}")
                    category_total += amount
                
                print(f"  Total for {category}: ${category_total:.2f}")
                
    elif choice == "4":
        print("Thanks for using the Expense Tracker! 💰")
        break  # This exits the while loop
    else:
        print("❌ Invalid choice! Please enter 1, 2, 3, or 4.")
