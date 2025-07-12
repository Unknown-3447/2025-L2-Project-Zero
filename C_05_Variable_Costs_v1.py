import pandas


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

        # check datatype is correct and that number is more than zero
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


def get_expenses(exp_type, how_many):
    """Gets variable / fixed expenses and outputs panda (as a string) and a subtotal of the expenses"""

    # Lists for pandas
    all_items = []
    all_amounts = []
    all_dollar_per_item = []

    # Expenses dictionary
    expenses_dict = {
        "Item": all_items,
        "Amount": all_amounts,
        "$ / Item": all_dollar_per_item
    }

    # loop to get expenses
    while True:
        # Get item name and check it's not blank
        item_name = not_blank("Item Name (or 'xxx' to stop): ")

        # check user enters at least one variable expense
        if ((exp_type == "variable" and item_name == "xxx")
                and len(all_items) == 0):
            print("Oops - you have not entered anything.  "
                  "You need at least one item.")
            continue
        elif item_name == "xxx":
            break

        # Get item amount
        amount = num_check(f"How many <enter for {how_many}>: ",
                           "integer", exit_code="")

        if amount == "":
            amount = how_many
        else:
            amount = int(amount)  # Make sure amount is an int

        # Get cost per item
        cost = num_check("Price for one? $", "float")

        # Add to lists
        all_items.append(item_name)
        all_amounts.append(amount)
        all_dollar_per_item.append(cost)

    # Create DataFrame
    expense_frame = pandas.DataFrame(expenses_dict)

    # Calculate Cost column
    expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['$ / Item']

    # Calculate subtotal
    subtotal = expense_frame['Cost'].sum()

    return expense_frame, subtotal


# Main Routine

quantity_made = num_check("Quantity being made: ", "integer")
print()

print("Getting Variable Costs...")
variable_expenses = get_expenses("variable", quantity_made)
print()

# Unpack results
variable_panda = variable_expenses[0]
variable_subtotal = variable_expenses[1]

# Output results
print(variable_panda)
print(f"\nVariable Expenses Subtotal: ${variable_subtotal:.2f}")
