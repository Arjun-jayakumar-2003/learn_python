number_list = []

list_size = int(input("Enter how many number are going to be there: "))
print("Enter the numbers to check which is the largest number")
for i in range(list_size):
    value = int(input("Enter the number: "))
    number_list.append(value)
largest_value = 0
if number_list[0] > number_list[1]:
    largest_value = number_list[0]
else:
    largest_value = number_list[1]
i = 2
for i in range(list_size):
    if largest_value < number_list[i]:
        largest_value = number_list[i]
print("The largest value entered is " + str(largest_value))
