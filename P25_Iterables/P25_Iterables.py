
"""
numbers = [1, 2, 3, 4, 5]

# for number in numbers:
#     print(number)

for number in reversed(numbers):
    print(number, end=" - ")
"""


"""
numbers = (1, 2, 3, 4, 5)
for number in numbers:
    print(number)
"""


"""
fruits = {"apple", "orange", "banana", "pineapple"}
for fruit in fruits:            # set objects are not reversible
    print(fruit)
"""

""" # strings
name = "Alex Smith"
for char in name:
#     print(char)
    print(char, end=" ")
"""


""" # Dictionaries

"""
my_dictionary = {"A": 1, "B": 2, "C": 3}

# for key in my_dictionary:
#     print(key)

for key, value in my_dictionary.items():
    print(f"{key} = {value}")