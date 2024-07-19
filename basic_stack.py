stack = []
stack_length = 0


def push():
    global stack
    global stack_length
    if len(stack) >= stack_length:
        print("STACK IS FULL!\nCAN'T PUSH")
    else:
        item = int(input("Enter the item: "))
        stack.append(item)
        print(f"Item {item} pushed to stack")


def pop():
    global stack
    if len(stack) == 0:
        print("STACK IS EMPTY!\nCAN'T POP")
    else:
        item = stack.pop()
        print(f"Item {item} popped out from stack")


def main():
    print("Basic Stack Operations")
    global stack_length
    while 1:
        stack_length = int(input("Enter the stack size: "))
        while 1:
            operation = int(input("Enter the operation to perform on the stack"
                                  "\n1.PUSH\n2.POP\n3.RESTART\noperation:  "))
            if operation == 1:
                push()
            elif operation == 2:
                pop()
            elif operation == 3:
                break
            else:
                print("ERROR! INVALID OPERATION")
        continue_operation = input("Do you wish to continue(yes/no): ")
        if continue_operation != 'yes':
            break


if __name__ == "__main__":
    main()
