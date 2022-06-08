#Calculator
from art import logo
#Addition
def add(x, y):
    return x + y

#Subtraction
def sub(x, y):
    return x - y

#Multiplication
def mult(x, y):
    return x * y

#Division
def div(x, y):
    return x / y

#Dictionary for all Operations:
operations = {
    "+": add,
    "-": sub,
    "*": mult,
    "/": div,
}

def calculator():
    print(logo)
    running = True
    num1 = float(input("What is the first number?: "))

    while running:
        num2 = float(input("What is the second number?: "))
        for symbols in operations:
            print(symbols)
        operation_symbol = input("Pick an opertation from the line above: ")
        solution = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {solution}")

        if input(f"Type 'y' to continue calculating with {solution}, or type 'n' to start a new calculation: ") == "y":
            num1 = solution
        else:
            running = False
            calculator()

calculator()
