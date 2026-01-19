# Strings

"""
fruits = ["apple", "orange", "banana", "coconut"]
fruits = [fruit.upper() for fruit in fruits]
print(fruits)
"""


"""
fruits = [fruit.upper() for fruit in ["apple", "orange", "banana", "coconut"]]
print(fruits)
"""

"""
fruits = ["apple", "orange", "banana", "coconut"]
fruit_chars = [fruit[0] for fruit in fruits]
print(fruit_chars)
"""

numbers = [1, -2, 3, -4, 5, -6, -7, 8]
positive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num %2 == 0]
odd_nums = [num for num in numbers if num %2 == 1]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)