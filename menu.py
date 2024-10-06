'''Base menu with options'''

def displayMenu():
    print("Choose one of the following options: ")
    print("1. Add two numbers")
    print("2. Multiply two numbers")
    print("0. Quit")
    choice = int(input())
    return choice
