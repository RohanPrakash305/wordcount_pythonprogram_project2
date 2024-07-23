import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox

# Function to get user input from the console
def get_user_input():
    """
    Prompts the user to input expense details and returns them.

    Returns:
        date (str): The date of the expense in YYYY-MM-DD format.
        amount (float): The amount spent.
        category (str): The category of the expense.
        description (str): A brief description of the expense.
    """
    date = input("Enter the date (YYYY-MM-DD): ")
    amount = float(input("Enter the amount spent: "))
    category = input("Enter the category (e.g., food, transportation): ")
    description = input("Enter a brief description: ")
    return date, amount, category, description

# Function to save expenses to a CSV file
def save_expenses(expenses, filename='expenses.csv'):
    """
    Saves the list of expenses to a CSV file.

    Args:
        expenses (list of dict): The list of expenses to save.
        filename (str): The name of the CSV file to save the expenses to.
    """
    df = pd.DataFrame(expenses)
    df.to_csv(filename, index=False)

# Function to load expenses from a CSV file
def load_expenses(filename='expenses.csv'):
    """
    Loads expenses from a CSV file and returns them as a list of dictionaries.

    Args:
        filename (str): The name of the CSV file to load the expenses from.

    Returns:
        list of dict: The list of expenses loaded from the file.
    """
    try:
        df = pd.read_csv(filename)
        return df.to_dict('records')
    except FileNotFoundError:
        return []

# Function to add a new expense to the list and save it
def add_expense(date, amount, category, description):
    """
    Adds a new expense to the list and saves it to the CSV file.

    Args:
        date (str): The date of the expense.
        amount (float): The amount spent.
        category (str): The category of the expense.
        description (str): A brief description of the expense.
    """
    try:
        amount = float(amount)
        new_expense = {'Date': date, 'Amount': amount, 'Category': category, 'Description': description}
        expenses.append(new_expense)
        save_expenses(expenses)
    except ValueError:
        print("Invalid amount. Please enter a number.")

# Function to summarize expenses by category
def summarize_expenses():
    """
    Summarizes the total amount spent in each category and prints it.
    """
    df = pd.DataFrame(expenses)
    summary = df.groupby('Category').sum()
    print(summary)

# Function to plot expenses by category
def plot_expenses():
    """
    Plots the total amount spent in each category as a bar chart.
    """
    df = pd.DataFrame(expenses)
    summary = df.groupby('Category').sum()
    summary.plot(kind='bar')
    plt.show()

# Load existing expenses
expenses = load_expenses()

# GUI setup
def submit_expense():
    """
    Submits the expense entered in the GUI and shows a success message.
    """
    date = date_entry.get()
    amount = amount_entry.get()
    category = category_entry.get()
    description = description_entry.get()
    add_expense(date, amount, category, description)
    messagebox.showinfo("Success", "Expense added successfully!")

root = tk.Tk()
root.title("Expense Tracker")

# GUI layout
tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=0)
tk.Label(root, text="Amount").grid(row=1)
tk.Label(root, text="Category").grid(row=2)
tk.Label(root, text="Description").grid(row=3)

date_entry = tk.Entry(root)
amount_entry = tk.Entry(root)
category_entry = tk.Entry(root)
description_entry = tk.Entry(root)

date_entry.grid(row=0, column=1)
amount_entry.grid(row=1, column=1)
category_entry.grid(row=2, column=1)
description_entry.grid(row=3, column=1)

tk.Button(root, text='Add Expense', command=submit_expense).grid(row=4, column=1, sticky=tk.W, pady=4)
tk.Button(root, text='Quit', command=root.quit).grid(row=4, column=0, sticky=tk.W, pady=4)

root.mainloop()
