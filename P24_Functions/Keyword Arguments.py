
"""
def hello(greetings, title, first, last):
    print(f"{greetings} {title} {first} {last}")

# hello("Hello", "Mr.", "Alex", "Smith")
# hello("Hello", "Alex", "Smith", "Mr.")
hello("Hello", "Mr.", last="Smith", first="Alex")

"""

# for x in range(1, 11):
#     print(x, end=" ")

# print("1", "2", "3", "4", "5", sep="-")

### exercise

def get_phone(country, area, first, last):
    return f"+{country} {area}-{first}-{last}"

phone_num = get_phone(country=91, area=123, first=456, last=7890)
print(phone_num)