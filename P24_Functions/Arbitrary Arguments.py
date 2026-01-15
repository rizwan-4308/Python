### *args
"""
def add(a, b):
    return a + b

# print(add(1, 2))
# print(add(1, 2, 3))
"""

"""
def add(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(add(1, 2, 3, 5, 6, 7))

"""

"""
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(add(1, 2, 3, 5, 6))

"""

def display_name(*args):
    for arg in args:
        print(arg, end=" ")

display_name("Dr.", "Alex", "L.", "Smith")
