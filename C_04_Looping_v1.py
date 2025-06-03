# Initialise ticket numbers
MAX_TICKETS = 5
tickets_sold = 0

while tickets_sold < MAX_TICKETS:
    name = input("Enter name (or 'xxx' to quit): ").strip()

    # Check for exit code
    if name.lower() == "xxx":
        break

    # Check for blank name
    if name == "":
        print("Name can't be blank. Please try again.")
        continue

    tickets_sold += 1
    print(f"Ticket sold to {name}. ({tickets_sold} / {MAX_TICKETS} tickets sold)\n")

# Output final message
print()
if tickets_sold == MAX_TICKETS:
    print(f"All tickets sold! ({MAX_TICKETS} tickets total)")
else:
    print(f"You sold {tickets_sold} / {MAX_TICKETS} tickets.")
