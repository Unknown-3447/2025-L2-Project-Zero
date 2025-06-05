# Functions go here
def string_check(question, valid_ans_list, num_letters):
    """
    Checks that users enter the full word or the first 'n' letters of a valid response.
    """

    while True:
        response = input(question).strip().lower()

        for item in valid_ans_list:
            # Check for full word match or valid shortcut
            if response == item or response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_ans_list}.\n")


# Main routine goes here
yes_no_list = ['yes', 'no']
payment_list = ['cash', 'credit']

like_coffee = string_check("Do you like coffee? (yes/no): ", yes_no_list, 1)
print(f"You chose: {like_coffee}")

pay_method = string_check("Payment method (cash/credit): ", payment_list, 2)
print(f"You chose: {pay_method}")
