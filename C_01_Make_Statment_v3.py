# Functions go here
def make_statement(statement, decoration, lines):
    """Creates headings:
    - 3 lines: heading (top, middle, bottom)
    - 2 lines: subheading (middle + underline)
    - 1 line: emphasised/mini heading (emoji style)

    Only use emojis or short symbols for single-line headings.
    """

    middle = f"{decoration * 3} {statement} {decoration * 3}"
    top_bottom = decoration * len(middle)

    if lines == 1:
        print(middle)
    elif lines == 2:
        print(middle)
        print(top_bottom)
    elif lines == 3:
        print(top_bottom)
        print(middle)
        print(top_bottom)
    else:
        print("Error: 'lines' must be 1, 2, or 3.")


# Main Routine goes here
make_statement("Programming is Fun!", "=", 3)
print()
make_statement("Programming is Still Fun!", "*", 2)
print()
make_statement("Emoji in Action", '🐍', 1)
print()
make_statement("Oops!", "!", 4)  # Invalid line number example
