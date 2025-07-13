def yes_no(question):
    while True:
        response = input(question).strip().lower()
        if response in ("yes", "y"):
            return "yes"
        elif response in ("no", "n"):
            return "no"
        else:
            print("Please enter yes (y) or no (n).\n")


def profit_goal(total_costs):
    """Calculates profit goal and total sales required"""
    error = "Please enter a valid profit goal\n"

    valid = False
    while not valid:

        response = input("What is your profit goal (eg $500 or 50%): ").strip()

        # Check if first character is $
        if response.startswith("$"):
            profit_type = "$"
            amount = response[1:]

        # Check if last character is %
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
            dollar_type = yes_no(f"Do you mean ${amount:.2f} (i.e. {amount:.2f} dollars)? ")
            profit_type = "$" if dollar_type == "yes" else "%"

        elif profit_type == "unknown" and amount < 100:
            percent_type = yes_no(f"Do you mean {amount:.0f}%? ")
            profit_type = "%" if percent_type == "yes" else "$"

        # Return profit goal
        if profit_type == "$":
            return amount
        else:
            goal = (amount / 100) * total_costs
            return goal


# Main routine for testing...
while True:
    total_expenses = 200
    target = profit_goal(total_expenses)
    sales_target = total_expenses + target
    print(f"Profit Goal: ${target:.2f}")
    print(f"Sales Target: ${sales_target:.2f}")
    print()
