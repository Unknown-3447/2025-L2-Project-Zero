def not_blank(question):
    """Prompts the user until they enter a non-blank response."""

    while True:
        response = input(question).strip()

        if response:
            return response

        print("Sorry, this can't be blank. Please try again.\n")


# Main routine starts here
who = not_blank("Please enter your name: ")
print(f"Hello, {who}!")
