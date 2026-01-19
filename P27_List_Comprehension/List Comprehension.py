
"""
doubles = []
for x in range(1, 11):
    doubles.append(x * 2)

print(doubles)
"""

# we can use list comprehension
doubles = [x * 2 for x in range(1, 11)]
triples = [y * 3 for y in range(1, 11)]
squares = [z * z for z in range(1, 11)]

print(doubles)
print(triples)
print(squares)

