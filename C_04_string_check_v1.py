# Functions go here
def string_check(question, valid_ans_list):
    """Checks that users enter the full word or the first letter of a word
    from a list of valid responses"""

    while True:
        response = input(question).lower()

        for item in valid_ans_list:

            # Checks if the response is the entire word
            if response == item:
                return item

            # Checks if it's the first letter
            elif response == item[0]:
                return item

        print(f"Please choose a option from {valid_ans_list}")


# Main routine goes here
levels = ['easy', 'medium', 'hard']

like_coffee = string_check("Do you like coffee? ", ['yes', 'no'])
print(f"You chose {like_coffee}")
choose_level = string_check("Choose a level: ", levels)
print(f"You chose {choose_level}")
