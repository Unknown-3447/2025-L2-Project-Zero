# Functions go here

def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""
    print(f"{decoration * 3} {statement} {decoration * 3}")


def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word or the first 'n' letters of a valid response"""
    while True:
        response = input(question).lower()

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


# Main routine starts here
make_statement("Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions? ", ('yes', 'no'), 1)

if want_instructions == "yes":
    instructions()
else:
    print("Instructions skipped.")

print()
payment_ans = ('cash', 'credit')  # Changed to tuple for consistency
pay_method = string_check("Payment method: ", payment_ans, 2)
print(f"You chose {pay_method}")

print()
print("Program continues...")
