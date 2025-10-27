def main():
# Ask user for their name
    name = input("What is your name? ")
    hello(name)

def hello(to="world"):
# print the name or "world" is there is no input
    print("hello,", to)

main() 


