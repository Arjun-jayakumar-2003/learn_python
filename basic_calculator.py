def add():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    print(number1 + number2)


def sub():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    print(number1 - number2)


def mul():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    print(number1 * number2)


def div():
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    print(number1 / number2)


def main():
    print("BASIC CALCULATOR")
    print("Enter the operation to perform \n1.ADD\n2.SUBTRACT\n3.MULTIPLY\n4.DIVISION\n5.EXIT")
    while 1:
        operation = int(input("operation: "))
        if operation == 1:
            add()
        elif operation == 2:
            sub()
        elif operation == 3:
            mul()
        elif operation == 4:
            div()
        elif operation == 5:
            print("EXITED CALCULATOR")
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
