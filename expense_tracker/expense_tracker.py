import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Expense', 'Category', 'Amount'])

def add_expense():
    """Function to add a new expense"""
    date = input("Enter the date (YYYY-MM-DD): ")
    expense = input("Enter the expense description: ")
    category = input("Enter the category (e.g., Food, Transport, etc.): ")
    amount = float(input("Enter the amount: "))
    
    # Write data to CSV
    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, expense, category, amount])
    print("Expense added successfully!\n")

def view_expenses():
    """Function to view all expenses"""
    print("\nExpenses:")
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            print(f"Date: {row[0]}, Expense: {row[1]}, Category: {row[2]}, Amount: {row[3]}")
    print("\n")

def main():
    """Main function to interact with the user"""
    while True:
        print("Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
