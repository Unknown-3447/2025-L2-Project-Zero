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

        if exit_code and response.lower() == exit_code:
            return exit_code

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


def get_expenses(exp_type):
    """Gets variable or fixed expenses and returns items and subtotal"""
    all_items = []
    subtotal = 0

    while True:
        item_name = not_blank("Item Name (or 'xxx' to stop): ")

        if (exp_type == "variable" and item_name.lower() == "xxx") and len(all_items) == 0:
            print("Oops - you need to enter at least one item.")
            continue
        elif item_name.lower() == "xxx":
            break

        item_cost = num_check("Cost: $", "float")
        if exp_type == "variable":
            quantity = num_check("Quantity: ", "int")
        else:
            quantity = 1  # default quantity for fixed costs

        total = item_cost * quantity
        subtotal += total

        all_items.append({
            "Item": item_name,
            "Cost": item_cost,
            "Quantity": quantity,
            "Total": total
        })

    return all_items, subtotal


# Main Routine
print("Getting Variable Costs...")
variable_expenses, variable_subtotal = get_expenses("variable")
num_variable = len(variable_expenses)
print(f"\nYou entered {num_variable} variable item(s). Subtotal = ${variable_subtotal:.2f}")

# Optional: Uncomment to include fixed costs too
# print("\nGetting Fixed Costs...")
# fixed_expenses, fixed_subtotal = get_expenses("fixed")
# num_fixed = len(fixed_expenses)
# print(f"\nYou entered {num_fixed} fixed item(s). Subtotal = ${fixed_subtotal:.2f}")
