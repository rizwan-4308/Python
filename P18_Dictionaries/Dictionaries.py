
capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))

"""
if capitals.get("japan"):
    print("That capital does exists")
else:
    print("That capital does not exist")
"""

# capitals.update({"Germany": "Berlin"})
# capitals.update({"China": "Hongkong"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

""" # for every key in dict 
keys = capitals.keys()

for key in keys:
    print(key)

"""

# print(capitals)
# print(keys)

"""
# to get all the values in the dictionaries
values = capitals.values()
for value in values:
    print(value)
"""

""""  """
# items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")
