'''A simple project to practice making a modular menu that performs various functions based on input'''

# Import files, this allows you to use methods from them
from addition import *
from multiplication import *
from menu import *
from quit import *

def main():
    '''Main function that contains while loop'''
    running = True
    while (running):
        choice = displayMenu()
        if (choice == 1):
            add()

        elif (choice == 2):
            multiply()

        elif (choice == 0):
            running = quitProgram()

        else:
            print("Try Again")


if __name__ == '__main__':
    main()