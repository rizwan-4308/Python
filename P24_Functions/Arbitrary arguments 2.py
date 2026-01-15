

"""
def print_address(**kwargs):
    for value in kwargs.values():
        print(value)

"""

"""
def print_address(**kwargs):
    for key in kwargs.keys():
        print(key)
"""

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="123 Fake street",
              apt="100",
              city="Detroit",
              state="MI",
              zip="54321")