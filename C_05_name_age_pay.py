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


# Main routine goes here

# Initialise variables / valid options
payment_ans = ('cash', 'credit')

# Loop for testing purposes...
while True:
    print()

    # Ask user for their name (check it's not blank)
    name = not_blank("Name: ")

    # Ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue

    # Ask for payment method (cash / credit / ca / cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)

    # Confirm ticket purchase
    print(f"{name} has bought a ticket ({pay_method})")

