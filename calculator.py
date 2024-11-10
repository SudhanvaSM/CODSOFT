# Method to add two numbers.
def add (n1,n2):
    return n1+n2

# Method to subtract two numbers.
def subtract (n1,n2):
    return n1-n2

# Method to multiply two numbers.
def multiply (n1,n2):
    return n1*n2

# Method to divide two numbers.
def divide (n1,n2):
    return n1/n2

# Dictionary to list all the operations.
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

# Method to ask user's input and calculate result.
def main():
    should_continue = True
    num1 = float(input("Enter first number: "))

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: " )
        num2 = float(input("Enter second number: "))
        answer = operations[operation_symbol](num1,num2)
        print (f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start new calculation: ").lower()

        if choice == 'y':
            num1 = answer
        else:
            break
    main()

if __name__ == "__main__":
    main()