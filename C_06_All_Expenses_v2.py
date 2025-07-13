import pandas
from tabulate import tabulate


def not_blank(question):
    """Checks that a user response is not blank"""
    while True:
        response = input(question).strip()
        if response != "":
            return response
        print("Sorry, this can't be blank. Please try again.\n")


def num_check(question, num_type="float", exit_code=None):
    """Checks that response is a float / integer more than zero"""
    if num_type == "float":
        error = "Please enter a number more than 0."
    else:
        error = "Please enter an integer more than 0."

    while True:
        response = input(question)

        # check for exit code and return it if entered
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
    """Formats numbers as currency"""
    return "${:.2f}".format(x)


def get_expenses(exp_type, how_many=1):
    """Gets variable/fixed expenses and returns a formatted string and subtotal"""

    # Lists for pandas
    all_items = []
    all_amounts = []
    all_dollar_per_item = []

    # Expense dictionary
    expenses_dict = {
        "Item": all_items,
        "Amount": all_amounts,
        "$ / Item": all_dollar_per_item
    }

    while True:
        # Get item name and check it's not blank
        item_name = not_blank("Item Name (or 'xxx' to stop): ")

        # Force at least one variable item
        if exp_type == "variable" and item_name.lower() == "xxx" and len(all_items) == 0:
            print("Oops - you must enter at least one item.")
            continue
        elif item_name.lower() == "xxx":
            break

        # Get quantity (or default for fixed)
        if exp_type == "variable":
            amount = num_check(f"How many <enter for {how_many}>: ", "integer", exit_code="")
            if amount == "":
                amount = how_many
            else:
                amount = int(amount)
        else:
            amount = 1

        # Get price per item
        price_for_one = num_check("Price for one? $", "float")

        # Append to lists
        all_items.append(item_name)
        all_amounts.append(amount)
        all_dollar_per_item.append(price_for_one)

    # Create DataFrame
    expense_frame = pandas.DataFrame(expenses_dict)

    # Calculate total cost per item
    expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['$ / Item']

    # Calculate subtotal
    subtotal = expense_frame['Cost'].sum()

    # Format currency columns
    for column in ['Amount', '$ / Item', 'Cost']:
        expense_frame[column] = expense_frame[column].apply(currency)

    # Format the table using tabulate
    if exp_type == "variable":
        expense_string = tabulate(expense_frame, headers='keys',
                                  tablefmt='psql', showindex=False)
    else:
        expense_string = tabulate(expense_frame[['Item', 'Cost']], headers='keys',
                                  tablefmt='psql', showindex=False)

    return expense_string, subtotal


# ==== Main Routine ====

quantity_made = num_check("Quantity being made: ", "integer")
print()

# Get variable expenses
print("Getting Variable Costs...")
variable_expenses = get_expenses("variable", quantity_made)
print()
variable_panda = variable_expenses[0]
variable_subtotal = variable_expenses[1]

# Get fixed expenses
print("Getting Fixed Costs...")
fixed_expenses = get_expenses("fixed")
print()
fixed_panda = fixed_expenses[0]
fixed_subtotal = fixed_expenses[1]

# Output section
print("\n=== Variable Expenses ===")
print(variable_panda)
print(f"Variable subtotal: ${variable_subtotal:.2f}")

print("\n=== Fixed Expenses ===")
print(fixed_panda)
print(f"Fixed subtotal: ${fixed_subtotal:.2f}")

total_expenses = variable_subtotal + fixed_subtotal
print(f"\nTotal Expenses: ${total_expenses:.2f}")
