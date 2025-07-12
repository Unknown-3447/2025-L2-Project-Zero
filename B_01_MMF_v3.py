import pandas
import random  # For winner selection

# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""
    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word or the first 'n' letters of a valid response"""
    while True:
        response = input(question).lower().strip()
        for item in valid_answers:
            if response == item or response == item[:num_letters]:
                return item
        print(f"Please choose an option from {valid_answers}")


def instructions():
    make_statement("Instructions", "ℹ️")
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
    """Checks that a user response is not blank"""
    while True:
        response = input(question).strip()
        if response != "":
            return response
        print("Sorry, this can't be blank. Please try again.\n")


def int_check(question):
    """Checks users enter an integer"""
    error = "Oops - please enter an integer"
    while True:
        try:
            response = int(input(question))
            return response
        except ValueError:
            print(error)


def currency(x):
    """Formats numbers as currency"""
    return "${:.2f}".format(x)


# Main routine starts here
MAX_TICKETS = 5
tickets_sold = 0

# Valid payment options and pricing
payment_ans = ('cash', 'credit')
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50
CREDIT_SURCHARGE = 0.05

# Lists to hold ticket data
all_names = []
all_ticket_costs = []
all_surcharges = []

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_costs,
    'Surcharge': all_surcharges
}

# Program intro
make_statement("Mini-Movie Fundraiser Program", "🍿")

# Show instructions if requested
print()
want_instructions = string_check("Do you want to see the instructions? (yes/no): ", ('yes', 'no'), 1)
if want_instructions == "yes":
    instructions()
else:
    print("Instructions skipped.")

print()

# Ticket selling loop
while tickets_sold < MAX_TICKETS:
    print(f"\n--- Ticket {tickets_sold + 1} of {MAX_TICKETS} ---")

    name = not_blank("Name: ")

    if name.lower() == "xxx":
        break

    age = int_check("Age: ")

    # Determine ticket price based on age
    if age < 12:
        print(f"{name} is too young.")
        continue
    elif age > 120:
        print(f"{name} is too old.")
        continue
    elif age < 16:
        ticket_price = CHILD_PRICE
    elif age < 65:
        ticket_price = ADULT_PRICE
    else:
        ticket_price = SENIOR_PRICE

    pay_method = string_check("Payment method (cash/credit): ", payment_ans, 2)

    # Calculate surcharge
    if pay_method == "cash":
        surcharge = 0
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    # Store ticket data
    all_names.append(name)
    all_ticket_costs.append(ticket_price)
    all_surcharges.append(surcharge)

    tickets_sold += 1
    print(f"{name} has bought a ticket ({pay_method})")
    print(f"Ticket sold to {name}. ({tickets_sold} / {MAX_TICKETS} tickets sold)")

# Summary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Add calculated columns
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5  # $5 base cost

# Calculate totals before formatting
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

# Choose random winner
winner = random.choice(all_names)
winner_index = all_names.index(winner)

# Retrieve values before formatting
ticket_won = mini_movie_frame.at[winner_index, 'Total']
profit_won = mini_movie_frame.at[winner_index, 'Profit']

# Apply currency formatting to display
currency_fields = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for field in currency_fields:
    mini_movie_frame[field] = mini_movie_frame[field].apply(currency)

# Output results
print("\n--- Ticket Sales Summary ---")
print(mini_movie_frame.to_string(index=False))
print(f"\nTotal Paid:   ${total_paid:.2f}")
print(f"Total Profit: ${total_profit:.2f}")

# Winner announcement
print(f"\n🎉 The lucky winner is {winner}! Their ticket worth ${ticket_won:.2f} is free!")
print(f"Total Paid is now:   ${total_paid - ticket_won:.2f}")
print(f"Total Profit is now: ${total_profit - profit_won:.2f}")

print()
if tickets_sold == MAX_TICKETS:
    print(f"🎉 All tickets sold! ({MAX_TICKETS} tickets total)")
else:
    print(f"You sold {tickets_sold} / {MAX_TICKETS} tickets.")
