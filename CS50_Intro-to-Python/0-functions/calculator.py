
# x = 1
# y = 2
# x = input("What is x? ")
# y = input("What is y? ")

# integers
# z = int(x) + int(y)
# print(z)

# collect input and convert to integer in the same line
#x = int(input("What is x? "))
#y = int(input("What is y? "))

# print the result in one line.  still need error handing in case the user inputs a string rather than integers
#print(x + y)

# can also do it in one line, but you may sacrifice readability
# print(int(input("What is x? ")) + int(input("What is x? ")))

# floating point
x = float(input("What is x? "))
y = float(input("What is y? "))
# print(x + y)

# rounding to nearest integer or with a specific number of digits
z = round(x + y)
# division and round to a certain number of digits
# w = round(x / y, 2)
w = (x / y)

# add commas for long numbers with , as a seperator
# print(f"addition: {z:,}, division: {w:,}")

# division and round to a certain number of digits
print(f"addition: {z:,}, division: {w:.2f}")

