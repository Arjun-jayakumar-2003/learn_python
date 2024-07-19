def factorial(a):
    if a == 1:
        return a
    else:
        b = a * factorial(a - 1)
        return b


number = int(input("Enter the number whose factorial is needed: "))
result = factorial(number)
print("The factorial of the entered number is ", str(result))
