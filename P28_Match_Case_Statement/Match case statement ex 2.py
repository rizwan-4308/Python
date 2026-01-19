
"""
def is_weekend(day):
    match day:
        case "Sunday":
            return True
        case "Monday":
            return False
        case "Tuesday":
            return False
        case "Wednesday":
            return False
        case "Thursday":
            return False
        case "Friday":
            return False
        case "Saturday":
            return True
        case _:
            return False

print(is_weekend("Monday"))
print(is_weekend("Tuesday"))
print(is_weekend("Wednesday"))
print(is_weekend("Thursday"))
print(is_weekend("Saturday"))
print(is_weekend("Sunday"))
print(is_weekend("Pizza"))
"""

def is_weekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return False

print(is_weekend("Sunday"))
