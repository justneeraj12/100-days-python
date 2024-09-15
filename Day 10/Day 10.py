def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def calculator():
    should_accumulate = True
    #print(operations["*"](4,8))
    num1 = float(input("What is the first number?: "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operations_symbol = input("Pick an operation: ")
        num2 = float(input("What is the second number? "))
        result = operations[operations_symbol](num1, num2)
        print(f"{num1} {operations_symbol} {num2} = {result}")  

        choice = input("type Y to continue with {result}, or type N to start new calculations.").lower()
    

        if choice == "y":
            num1 = result
        else: 
            should_accumulate = False
            print("\n"*20)
            calculator()
calculator()
