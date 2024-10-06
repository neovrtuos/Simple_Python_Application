'''Function that multiplies two user numbers'''

def multiply():
    print("Enter two numbers seperated by a space")
    numbers = input()
    numList = numbers.split()
    num1 = int(numList[0])
    num2 = int(numList[1])
    product = num1 * num2
    print(f"{num1} * {num2} = {product}")