import csv
from datetime import date
##STEP 1
def log_expense():
    name = input("Enter your name: ")
    date_str = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the description: ")
    amount = float(input("Enter the amount spent: "))
    category = input("Enter the category: ")

    with open('C:\Aditya\College Code\VIPUL SIR\IA Assignment\Q7\expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, date_str, description, amount, category])

##STEP 2
import csv

def calculate_total_expenses():
    total_expenses = {}
    with open("D:\\Sem-5\\adv. python\\Vipul's py\\IA ASSIGNMENT\\All Codes\\Q7\\expenses.csv", mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            name, _, _, amount, _ = row
            if name not in total_expenses:
                total_expenses[name] = 0
            total_expenses[name] += float(amount)

    for name, expenses in total_expenses.items():
        print(f"{name}: Total Expenses: ${expenses:.2f}")

calculate_total_expenses()

##STEP 3
import csv
import matplotlib.pyplot as plt
from collections import defaultdict

def generate_expense_trends_chart():
    date_expenses = defaultdict(float)
    
    with open("D:\\Sem-5\\adv. python\\Vipul's py\\IA ASSIGNMENT\\All Codes\\Q7\\expenses.csv", mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            _, date_str, _, amount, _ = row
            date_expenses[date_str] += float(amount)

    dates = list(date_expenses.keys())
    expenses = [date_expenses[date] for date in dates]

    plt.plot(dates, expenses)
    plt.xlabel('Date')
    plt.ylabel('Cumulative Expenses')
    plt.title('Expense Trends over the Last Month')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

generate_expense_trends_chart()

##STEP 4
import csv
from datetime import date

def log_expense():
    name = input("Enter your name: ")
    date_str = input("Enter the date (YYYY-MM-DD): ")
    description = input("Enter the description: ")
    amount = float(input("Enter the amount spent: "))
    category = input("Enter the category: ")

    with open('expenses.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, date_str, description, amount, category])

#STEP 5
import csv

def generate_expense_report():
    # Read the CSV file and calculate the monthly expenses report.
    expenses_by_name = {}
    expenses_by_category = {}

    with open("D:\\Sem-5\\adv. python\\Vipul's py\\IA ASSIGNMENT\\All Codes\\Q7\\expenses.csv", mode='r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row

        for row in reader:
            name, _, _, amount, category = row
            amount = float(amount)

            # Total expenses by family member
            if name not in expenses_by_name:
                expenses_by_name[name] = 0
            expenses_by_name[name] += amount

            # Total expenses by category
            if category not in expenses_by_category:
                expenses_by_category[category] = 0
            expenses_by_category[category] += amount

    # Display the report
    print("Monthly Expense Report:")
    for name, total in expenses_by_name.items():
        print(f"{name}: Total Expenses: ${total:.2f}")
    
    print("\nExpense Breakdown by Category:")
    for category, total in expenses_by_category.items():
        print(f"{category}: Total Expenses: ${total:.2f}")

generate_expense_report()


##STEP 6
import csv
from collections import defaultdict

def set_budget():
    category = input("Enter the category for budgeting: ")
    budget = float(input("Enter the monthly budget for this category: "))

    # Store the budget in a separate CSV file or data structure for tracking

def check_budget():
    # Calculate remaining budgets for categories and provide warnings if exceeded
    pass

##STEP 7
import shutil

def backup_expenses():
    # Create a backup copy of the expenses.csv file in a backup folder.
    backup_folder = "D:\Sem-5\adv. python\Vipul's py\IA ASSIGNMENT\All Codes\Q7\BACKKK"
    try:
        shutil.copy("D:\Sem-5\adv. python\Vipul's py\IA ASSIGNMENT\All Codes\Q7", backup_folder)
        print("Expense data backed up successfully.")
    except FileNotFoundError:
        print("Expense data file not found. Backup failed.")

def restore_expenses():
    # Restore the expenses.csv file from the backup folder.
    backup_folder = "D:\Sem-5\adv. python\Vipul's py\IA ASSIGNMENT\All Codes\Q7\BACKKK"
    try:
        shutil.copy(f'{backup_folder}/expenses.csv', 'expenses.csv')
        print("Expense data restored successfully.")
    except FileNotFoundError:
        print("Backup data file not found. Restore failed.")

#call the functions
log_expense()
calculate_total_expenses()
generate_expense_trends_chart()
generate_expense_report()
set_budget()
check_budget()
backup_expenses()
restore_expenses()
