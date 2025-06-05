# Functions go here
def string_check(question, valid_ans_list):
    """
    Checks that users enter either the full word or the first letter of a word
    from a list of valid responses.
    """

    while True:
        response = input(question).strip().lower()

        for item in valid_ans_list:
            # Checks if the response is the full word or first letter
            if response == item or response == item[0]:
                return item

        print(f"Please choose an option from {valid_ans_list}.\n")


# Main routine goes here
levels = ['easy', 'medium', 'hard']

like_coffee = string_check("Do you like coffee? (yes/no): ", ['yes', 'no'])
print(f"You chose: {like_coffee}")

choose_level = string_check("Choose a level (easy/medium/hard): ", levels)
print(f"You chose: {choose_level}")
