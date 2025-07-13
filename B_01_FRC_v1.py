import pandas
from tabulate import tabulate
from datetime import date  # fixed typo

# Functions
def make_statement(statement, decoration):
    return f"{decoration * 3} {statement} {decoration * 3}"

def yes_no(question):
    while True:
        response = input(question).strip().lower()
        if response in ("yes", "y"):
            return "yes"
        elif response in ("no", "n"):
            return "no"
        else:
            print("Please enter yes (y) or no (n).\n")

def instructions():
    print(make_statement("Instructions", "ℹ️"))
    print('''
For each Ticket holder enter...
- Their name
- Their age
- The payment method (cash / credit)

The program will record the ticket sale and calculate the ticket cost (and the profit).

Once you have either sold all of the tickets or entered the exit code ('xxx'), 
the program will display the ticket sales information and write the data to a text file.

It will also choose one lucky ticket holder who wins the draw (their ticket is free).
''')

def not_blank(question):
    while True:
        response = input(question).strip()
        if response != "":
            return response
        print("Sorry, this can't be blank. Please try again.\n")

def num_check(question, num_type="float", exit_code=None):
    if num_type == "float":
        error = "Please enter a number more than 0."
    else:
        error = "Please enter an integer more than 0."

    while True:
        response = input(question)

        if exit_code is not None and response == exit_code:
            return response

        try:
            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)

def currency(x):
    return "${:.2f}".format(x)

def get_expenses(exp_type, how_many=1):
    all_items = []
    all_amounts = []
    all_dollar_per_item = []

    expenses_dict = {
        "Item": all_items,
        "Amount": all_amounts,
        "$ / Item": all_dollar_per_item
    }

    while True:
        item_name = not_blank("Item Name (or 'xxx' to stop): ")

        if exp_type == "variable" and item_name.lower() == "xxx" and len(all_items) == 0:
            print("Oops - you must enter at least one item.")
            continue
        elif item_name.lower() == "xxx":
            break

        if exp_type == "variable":
            amount = num_check(f"How many <enter for {how_many}>: ", "integer", exit_code="")
            if amount == "":
                amount = how_many
            else:
                amount = int(amount)
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

    if exp_type == "variable":
        expense_string = tabulate(expense_frame, headers='keys', tablefmt='psql', showindex=False)
    else:
        expense_string = tabulate(expense_frame[['Item', 'Cost']], headers='keys', tablefmt='psql', showindex=False)

    return expense_string, subtotal

# ==== Main Routine ====
fixed_subtotal = 0
fixed_panda_string = ""

print(make_statement("Fund Raising Calculator", "💰"))

print()
want_instructions = yes_no("Do you want to see the instructions?")
print()
if want_instructions == "yes":
    instructions()

print()

product_name = not_blank("Product Name: ")
quantity = num_check("Quantity being made: ", "integer")

print("Let's get the variable expenses....")
variable_expenses = get_expenses("variable", quantity)

variable_panda_string = variable_expenses[0]
variable_subtotal = variable_expenses[1]

print()
has_fixed = yes_no("Do you have a fixed expense?")

if has_fixed == "yes":
    fixed_expenses = get_expenses("fixed")
    fixed_panda_string = fixed_expenses[0]
    fixed_subtotal = fixed_expenses[1]

    if fixed_subtotal == 0:
        has_fixed = "no"
        fixed_panda_string = ""

total_expenses = variable_subtotal + fixed_subtotal
total_expenses_string = f"Total Expenses ${total_expenses:.2f}"

# Date details
today = date.today()
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# Output Strings
main_heading_string = make_statement(f"Fund Raising Calculator - {product_name}, {day}/{month}/{year}", "=")
quantity_string = f"Quantity being made: {quantity}"
variable_heading_string = make_statement("Variable Expenses", "-")
variable_subtotal_string = f"Variable Expenses Subtotal: ${variable_subtotal:.2f}"

if has_fixed == "yes":
    fixed_heading_string = make_statement("Fixed Expenses", "-")
    fixed_subtotal_string = f"Fixed Expenses Subtotal: ${fixed_subtotal:.2f}"
else:
    fixed_heading_string = make_statement("You have no Fixed Expenses", "-")
    fixed_subtotal_string = "Fixed Expenses Subtotal: $0.00"

to_write = [main_heading_string, quantity_string,
            "\n", variable_heading_string, variable_panda_string,
            variable_subtotal_string,
            "\n", fixed_heading_string, fixed_panda_string,
            fixed_subtotal_string, total_expenses_string]

print()
for item in to_write:
    print(item)

file_name = f"{product_name}_{year}_{month}_{day}.txt"
with open(file_name, "w") as text_file:
    for item in to_write:
        text_file.write(item + "\n")
