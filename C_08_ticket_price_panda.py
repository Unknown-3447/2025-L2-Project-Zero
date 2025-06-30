import pandas

# Functions go here
def int_check(question):
    """Checks users enter an integer"""
    error = "Oops - please enter an integer"
    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""
    while True:
        response = input(question)
        if response.strip() != "":
            return response
        print("Sorry, this can't be blank. Please try again.\n")


def string_check(question, valid_ans_list=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word or the first letter of a word
    from a list of valid responses"""
    while True:
        response = input(question).lower()
        for item in valid_ans_list:
            if response == item or response == item[:num_letters]:
                return item
        print(f"Please choose an option from {valid_ans_list}")


# Currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Main routine starts here

# Initialise valid options and pricing
payment_ans = ('cash', 'credit')
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50
CREDIT_SURCHARGE = 0.05

# Lists to hold ticket data
all_names = []
all_ticket_costs = []
all_surcharges = []

# Ask user for ticket information
name = not_blank("Name: ")
age = int_check("Age: ")

# Determine ticket price
if age < 12:
    print(f"{name} is too young for a ticket.")
    exit()
elif age < 16:
    ticket_price = CHILD_PRICE
elif age < 65:
    ticket_price = ADULT_PRICE
elif age <= 120:
    ticket_price = SENIOR_PRICE
else:
    print(f"{name} is too old for a ticket.")
    exit()

# Ask for payment method
pay_method = string_check("Payment method (cash/credit): ", payment_ans, 2)

# Calculate surcharge
surcharge = 0
if pay_method == "credit":
    surcharge = ticket_price * CREDIT_SURCHARGE

# Store data
all_names.append(name)
all_ticket_costs.append(ticket_price)
all_surcharges.append(surcharge)

# Create DataFrame
mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_costs,
    'Surcharge': all_surcharges
}
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Add calculated columns before formatting
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5  # Assuming $5 cost per ticket

# Totals (must happen before formatting the DataFrame)
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

# Apply currency formatting
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

# Output results
print("\n--- Ticket Sales Summary ---")
print(mini_movie_frame.to_string(index=False))
print(f"\nTotal Paid:   ${total_paid:.2f}")
print(f"Total Profit: ${total_profit:.2f}")
