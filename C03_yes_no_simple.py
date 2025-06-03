# Functions go here
def yes_no(question):
    """Checks that users enter yes / y or no / n to a question"""

    while True:
        response = input(question).strip().lower()

        if response in ("yes", "y"):
            return "yes"
        elif response in ("no", "n"):
            return "no"
        else:
            print("Please enter yes (y) or no (n).\n")


# Main routine goes here

# Loop for testing purposes
while True:
    want_instructions = yes_no("Do you want to read the instructions? (yes/no): ")
    print(f"You chose: {want_instructions}\n")
