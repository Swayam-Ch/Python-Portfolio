import art
print(art.logo)
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

calculations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

result = 0
continue_calculating = True
first_number = int(input("Type the first number\n"))
while continue_calculating:
    operation = input("Type a mathematical operator + , -, * or /\n")
    second_number = int(input("Type the second number\n"))
    if operation == "+":
        result = calculations["+"](n1=first_number, n2=second_number)
    elif operation == "-":
        result = calculations["-"](n1=first_number, n2=second_number)
    elif operation == "*":
        result = calculations["*"](n1=first_number, n2=second_number)
    elif operation == "/":
        result = calculations["/"](n1=first_number, n2=second_number)
    print(f"The result is: {result}")

    question = input(f"Do you want to continue working with the previous number: {result}\n")
    if question == "yes":
        first_number = result
        continue_calculating = True
    elif question == "no":
        first_number = int(input("Type the first number\n"))
        continue_calculating = True




