
"""
fruits =      ["apple", "banana", "orange", "mango"]
vegetables =  ["celery" , "carrot", "potatoes"]
meats =       ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
"""


# print(fruits)
# print(vegetables)
# print(meats)

# print(groceries)

"""
print(groceries[0])
print(groceries[1])
print(groceries[2])
"""

"""
print(groceries[0][0])
print(groceries[0][1])
print(groceries[0][2])
print(groceries[0][3])
print(groceries[1][0])
print(groceries[1][1])
print(groceries[1][2])
print(groceries[2][0])
print(groceries[2][1])
print(groceries[2][2])
"""

groceries = [("apple", "banana", "orange", "mango"),
             ("celery", "carrot", "potatoes"),
             ("chicken", "fish", "turkey")]

# print(groceries)

"""
for collection in groceries:
    print(collection)
"""

"""
for collection in groceries:
    for food in collection:
        print(food)
"""

""" """
for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()
