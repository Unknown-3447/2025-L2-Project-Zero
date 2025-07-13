import pandas
import random
from tabulate import tabulate
from datetime import date
import math

# Functions
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""
    return f"{decoration * 3} {statement} {decoration * 3}"

def yes_no(question):
    """Checks for yes/y or no/n responses"""
    while True:
        response = input(question).strip().lower()
        if response in ("yes", "y"):
            return "yes"
        elif response in ("no", "n"):
            return "no"
        else:
            print("Please enter yes (y) or no (n).\n")

def string_check(question, valid_answers, num_letters=1):
    """Checks for valid string responses"""
    while True:
        response = input(question).lower().strip()
        for item in valid_answers:
            if response == item or response == item[:num_letters]:
                return item
        print(f"Please choose an option from {valid_answers}.")

def not_blank(question):
    """Checks that response is not blank"""
    while True:
        response = input(question).strip()
        if response:
            return response
        print("Sorry, this can't be blank. Please try again.\n")

def num_check(question, num_type="float", exit_code=None):
    """Checks for valid number input"""
    error = "Please enter a number more than 0." if num_type == "float" else "Please enter an integer more than 0."
    while True:
        response = input(question)
        if exit_code and response.lower() == exit_code:
            return response
        try:
            response = float(response) if num_type == "float" else int(response)
            if response > 0:
                return response
            print(error)
        except ValueError:
            print(error)

def currency(x):
    """Formats numbers as currency"""
    return "${:.2f}".format(x)

def get_expenses(exp_type, how_many=1):
    """Gets expenses and returns formatted table and subtotal"""
    all_items, all_amounts, all_dollar_per_item = [], [], []
    expenses_dict = {"Item": all_items, "Amount": all_amounts, "$ / Item": all_dollar_per_item}
    while True:
        item_name = not_blank("Item Name (or 'xxx' to stop): ")
        if exp_type == "variable" and item_name.lower() == "xxx" and not all_items:
            print("Oops - you must enter at least one item.")
            continue
        elif item_name.lower() == "xxx":
            break
        if exp_type == "variable":
            amount = num_check(f"How many: ", "integer", exit_code="")
            amount = how_many if amount == "" else int(amount)
        else:
            amount = 1
        price_for_one = num_check("Price for one? $", "float")
        all_items.append(item_name)
        all_amounts.append(amount)
        all_dollar_per_item.append(price_for_one)
    expense_frame = pandas.DataFrame(expenses_dict)
    expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['$ / Item']
    subtotal = expense_frame['Cost'].sum()
    for column in ['Amount', '$ / Item', 'Cost']:
        expense_frame[column] = expense_frame[column].apply(currency)
    expense_string = tabulate(expense_frame, headers='keys', tablefmt='psql', showindex=False) if exp_type == "variable" else tabulate(expense_frame[['Item', 'Cost']], headers='keys', tablefmt='psql', showindex=False)
    return expense_string, subtotal

def profit_goal(total_costs):
    """Calculates profit goal"""
    error = "Please enter a valid profit goal\n"
    while True:
        response = input("What is your profit goal (eg $500 or 50%): ").strip()
        if response.startswith("$"):
            profit_type = "$"
            amount = response[1:]
        elif response.endswith("%"):
            profit_type = "%"
            amount = response[:-1]
        else:
            profit_type = "unknown"
            amount = response
        try:
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue
        except ValueError:
            print(error)
            continue
        if profit_type == "unknown" and amount >= 100:
            profit_type = "$" if yes_no(f"Do you mean ${amount:.2f}? ") == "yes" else "%"
        elif profit_type == "unknown" and amount < 100:
            profit_type = "%" if yes_no(f"Do you mean {amount:.0f}%? ") == "yes" else "$"
        return amount if profit_type == "$" else (amount / 100) * total_costs

def round_up(amount, round_val):
    """Rounds amount up to nearest specified value"""
    return int(math.ceil(amount / round_val)) * round_val

# Main Routine
MAX_TICKETS = 50
CHILD_PRICE = 8.00
ADULT_PRICE = 12.00
SENIOR_PRICE = 6.00
CREDIT_SURCHARGE = 0.05
tickets_sold = 0
all_names, all_ticket_costs, all_surcharges = [], [], []
ticket_dict = {'Name': all_names, 'Ticket Price': all_ticket_costs, 'Surcharge': all_surcharges}
payment_ans = ('cash', 'credit')

# Program Intro
print(make_statement("Aquarium Ticket Fundraiser", "🐠"))
print()
if yes_no("Do you want to see the instructions? ") == "yes":
    print(make_statement("Instructions", "ℹ️"))
    print('''
For each visitor enter:
- Name
- Age (12-120 years)
- Payment method (cash/credit)
The program records ticket sales, calculates costs/profit, and picks a raffle winner.
Enter 'xxx' to stop and see the summary, saved to a file.
''')
else:
    print("Instructions skipped.")

# Get Expenses
print()
product_name = not_blank("Aquarium Event Name: ")
quantity = num_check("Number of tickets available: ", "integer")
print("\nEnter variable expenses (e.g., fish food, staff costs)...")
variable_expenses = get_expenses("variable", quantity)
variable_panda_string, variable_subtotal = variable_expenses
print()
has_fixed = yes_no("Do you have fixed expenses (e.g., tank maintenance)? ")
fixed_panda_string, fixed_subtotal = get_expenses("fixed") if has_fixed == "yes" else ("", 0)
total_expenses = variable_subtotal + fixed_subtotal
print()
target_profit = profit_goal(total_expenses)
sales_needed = total_expenses + target_profit
round_to = num_check("Round ticket prices to nearest (e.g., 1 for $1, 0.5 for 50c)? ", "float")
unrounded_price = sales_needed / quantity
recommended_price = round_up(unrounded_price, round_to)

# Ticket Sales Loop
print()
while tickets_sold < MAX_TICKETS:
    print(f"\n--- Ticket {tickets_sold + 1} of {MAX_TICKETS} ---")
    name = not_blank("Name: ")
    if name.lower() == "xxx":
        break
    age = num_check("Age: ", "integer")
    if age < 12:
        print(f"{name} is too young.")
        continue
    elif age > 120:
        print(f"{name} is too old.")
        continue
    ticket_price = CHILD_PRICE if age < 16 else SENIOR_PRICE if age >= 65 else ADULT_PRICE
    pay_method = string_check("Payment method (cash/credit): ", payment_ans, 2)
    surcharge = 0 if pay_method == "cash" else ticket_price * CREDIT_SURCHARGE
    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)
    tickets_sold += 1
    print(f"{name} has bought a ticket ({pay_method})")

# Summary
ticket_frame = pandas.DataFrame(ticket_dict)
ticket_frame['Total'] = ticket_frame['Ticket Price'] + ticket_frame['Surcharge']
ticket_frame['Profit'] = ticket_frame['Ticket Price'] - 5
total_paid = ticket_frame['Total'].sum()
total_profit = ticket_frame['Profit'].sum()
winner = random.choice(all_names) if all_names else "No entries"
winner_index = all_names.index(winner) if all_names else None
ticket_won = ticket_frame.at[winner_index, 'Total'] if winner_index is not None else 0
profit_won = ticket_frame.at[winner_index, 'Profit'] if winner_index is not None else 0
for field in ['Ticket Price', 'Surcharge', 'Total', 'Profit']:
    ticket_frame[field] = ticket_frame[field].apply(currency)

# Output Strings
today = date.today()
file_name = f"{product_name}_{today.strftime('%Y_%m_%d')}.txt"
to_write = [
    make_statement(f"Aquarium Fundraiser - {product_name}", "="),
    f"\nNumber of tickets: {quantity}",
    make_statement("Variable Expenses", "-"),
    variable_panda_string,
    f"Variable Subtotal: ${variable_subtotal:.2f}",
    make_statement("Fixed Expenses", "-") if has_fixed == "yes" else make_statement("No Fixed Expenses", "-"),
    fixed_panda_string,
    f"Fixed Subtotal: ${fixed_subtotal:.2f}",
    f"\nTotal Expenses: ${total_expenses:.2f}",
    f"\nProfit Goal: ${target_profit:.2f}",
    f"Total Sales Needed: ${sales_needed:.2f}",
    f"Unrounded Ticket Price: ${unrounded_price:.2f}",
    f"Recommended Ticket Price: ${recommended_price:.2f}",
    make_statement("Ticket Sales", "-"),
    ticket_frame.to_string(index=False),
    f"\nTotal Paid: ${total_paid:.2f}",
    f"Total Profit: ${total_profit:.2f}",
    make_statement("Raffle Winner", "-"),
    f"Lucky Winner: {winner}. Their ticket worth ${ticket_won:.2f} is free!" if winner != "No entries" else "No raffle due to no ticket sales.",
    f"Adjusted Total Paid: ${total_paid - ticket_won:.2f}",
    f"Adjusted Total Profit: ${total_profit - profit_won:.2f}",
    make_statement(f"Sold {tickets_sold}/{MAX_TICKETS} tickets", "-") if tickets_sold < MAX_TICKETS else make_statement(f"All {MAX_TICKETS} tickets sold!", "-")
]

# Print and Write to File
print()
for item in to_write:
    print(item)
with open(file_name, "w") as text_file:
    for item in to_write:
        text_file.write(str(item) + "\n")