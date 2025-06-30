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


# Main routine starts here

# Initialise variables / valid options
payment_ans = ('cash', 'credit')
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50
CREDIT_SURCHARGE = 0.05  # ✅ This fixes your error

# Get user info
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
if pay_method == "cash":
    surcharge = 0
else:
    surcharge = ticket_price * CREDIT_SURCHARGE  # ✅ Now this works

# Calculate total payable
total_to_pay = ticket_price + surcharge

# Output summary
print(f"\n{name}'s ticket cost: ${ticket_price:.2f}")
print(f"Payment method: {pay_method} — Surcharge: ${surcharge:.2f}")
print(f"Total payable: ${total_to_pay:.2f}")
