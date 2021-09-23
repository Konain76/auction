def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculation():
    num1 = float(input("What's the first number?:"))
    for operator in operations:
        print(operator)
    end_of_calculation = False
    while not end_of_calculation:
        operation_symbol = input("Pick an operation : ")
        num2 = float(input("What's the next number?:"))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        cal = input(f" Type 'y' to continue calculating with {answer}, or Type 'n' to start new calculation.:").lower()
        if cal == 'y':
            num1 = answer
        elif cal == 'n':
            end_of_calculation = True
            calculation()


calculation()