# Functions go here
def int_check(question):
    """Checks users enter an integer"""

    error = "Oops - please enter an integer"

    while True:

        try:
            # Return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


while True:
    print()

    # ask user for their name
    name = input("Name: ")  # replace with call to 'not blank' function

    # Ask for their age and check it's between 12 and 120
    age = int_check("Age: ")

    # Output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue

    else:
        print(f"{name} bought a ticket")


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
    def string_check(question, valid_ans_list, num_letters):
        """Checks that users enter the full word or the first letter of a word
        from a list of valid responses"""

        while True:
            response = input(question).lower()

            for item in valid_ans_list:

                # Checks if the response is the entire word
                if response == item:
                    return item

                # Checks if it's the first letter
                elif response == item[:num_letters]:
                    return item

            print(f"Please choose a option from {valid_ans_list}")


# Main routine goes here

# initialise variables / non-default options for string checker
payment_ans = ('cash', 'credit')

# loop for testing purposes...
while True:
    print()

    # ask user for their name (and check it's not blank)
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
    else:
        pass

    # ask user for payment method (cash / credit / ca / cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)
    print(f"{name} has brought a ticket ({pay_method}")
