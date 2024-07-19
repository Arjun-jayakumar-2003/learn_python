term_length = int(input("Enter the term limit for the fibonacci series: "))
first_number = 0
second_number = 1
print("Fibonacci series....")
print(str(first_number), end=" ")
print(str(second_number), end=" ")
term_length -= 2
while term_length != 0:
    third_number = first_number + second_number
    print(str(third_number), end=" ")
    first_number = second_number
    second_number = third_number
    term_length -= 1
