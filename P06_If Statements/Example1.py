response = input("Would you like some food?: (Y/N)")

if response == "Y":
    print("Have some Food!")
else:
    print("No Food for you!")

name = input("Enter your name: ")

if name == "":
    print("You did not enter your name")
else:
    print(f"Hello {name}!")