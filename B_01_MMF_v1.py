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


# Main routine starts here

# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

# Valid payment options
payment_ans = ('cash', 'credit')

# Program intro
make_statement("Mini-Movie Fundraiser Program", "🍿")

# Show instructions if requested
print()
want_instructions = string_check("Do you want to see the instructions? (yes/no): ", ('yes', 'no'), 1)

if want_instructions == "yes":
    instructions()
else:
    print("Instructions skipped.")

# Ticket selling loop
print()
while tickets_sold < MAX_TICKETS:
    print(f"--- Ticket {tickets_sold + 1} of {MAX_TICKETS} ---")

    # Ask for name
    name = not_blank("Name: ")

    # Check for exit code
    if name.lower() == "xxx":
        break

    # Ask for age and validate
    age = int_check("Age: ")

    if age < 12:
        print(f"{name} is too young.")
        continue
    elif age > 120:
        print(f"{name} is too old.")
        continue

    # Ask for payment method
    pay_method = string_check("Payment method (cash/credit): ", payment_ans, 2)

    # Confirm ticket sale
    print(f"{name} has bought a ticket ({pay_method})")

    # Count the ticket
    tickets_sold += 1
    print(f"Ticket sold to {name}. ({tickets_sold} / {MAX_TICKETS} tickets sold)\n")

# Final message
print()
if tickets_sold == MAX_TICKETS:
    print(f"🎉 All tickets sold! ({MAX_TICKETS} tickets total)")
else:
    print(f"You sold {tickets_sold} / {MAX_TICKETS} tickets.")
