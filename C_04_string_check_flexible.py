# Functions go here
def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    """Checks that users enter the full word or the first 'n' letter/s of a word from a list of valid responses"""

    while True:
        response = input(question).lower().strip()

        for item in valid_answers:
            # Checks if the response is the entire word or the first 'n' letters
            if response == item or response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}.")


# Main routine goes here
yes_no_answers = ('yes', 'no')
payment_ans = ('cash', 'credit')

# Ask if the user wants instructions
want_instructions = string_check("Do you want to see the instructions? (yes/no): ", yes_no_answers, 1)
print(f"You chose: {want_instructions}")

# Ask for payment method
pay_method = string_check("Payment method (cash/credit): ", payment_ans, 2)
print(f"You chose: {pay_method}")
