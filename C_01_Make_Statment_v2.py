# Functions go here
def make_statement(statement, decoration, lines):
    """Creates headings:
    - 3 lines: full heading
    - 2 lines: subheading (middle + underline)
    - 1 line: emphasised text (emoji-style)

    Note: Use emoji or short characters for decoration when using 1-line mode.
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
        print("Error: 'lines' must be 1, 2, or 3")


# Main Routine goes here
make_statement("Programming is Fun!", "=", 3)
make_statement("Mini-Heading", "*", 2)
make_statement("🍿 Enjoy!", "🍿", 1)
make_statement("Invalid Test", "#", 4)  # Demonstrates error handling
