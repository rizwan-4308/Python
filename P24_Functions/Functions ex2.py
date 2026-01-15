
""""
def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of amount ${amount:.2f} is due: {due_date}")

display_invoice("Alex", 42.50, "01/01")
"""

# return

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("md", "rizwan")
print(full_name)