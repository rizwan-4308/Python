import random

"""
number = random.randint(1, 20)
print(number)
"""


low = 1
high = 100
options = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# number = random.randint(low, high)
# number = random.randint(low, 20)
# number = random.randint(75, high)

# number = random.random()
# print(number)

# option = random.choice(options)
# print(option)

random.shuffle(cards)
print(cards)
