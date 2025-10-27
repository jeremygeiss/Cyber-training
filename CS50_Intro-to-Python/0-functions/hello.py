# Ask user for their name
# name = input("What is your name? ")

# .split() to remove whitespace from string; .strip is a method
# name = name.strip()

# .title() to capitalize the string, the user's name
# name = name.title()

# split() to split the input into two variables
# first, last = name.split(" ")

#remove whitespace from string and capitalize
# name = name.strip().title()

# ask user for name, strip whitespace, and capitalize all at once
# name = input("What is your name? ").strip().title()

# Say hello to the user
# print("Hello, " + name)
# print("Hello,", name)
# escape character to print literal quotes: " "
# print("Hello, \"friend\"")
# print(f"Hello, {name}")

# ask user for name, strip whitespace, and capitalize all at once
name = input("What is your name? ").strip().title()
# seperate two variables, first and last name
first, last = name.split(" ")
# Say hello to the user
print(f"Hello, {first}")

