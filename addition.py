'''Function that adds two user numbers'''

def add():

    print("Enter two numbers seperated by a space")
    numbers = input()
    numList = numbers.split()
    num1 = int(numList[0])
    num2 = int(numList[1])
    sum = num1 + num2
    print(f"{num1} + {num2} = {sum}")