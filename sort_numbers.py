number_list = [2, 3, 0, 4, 8]
size = 5
temp = 0
for i in range(0, size):
    for j in range(i + 1, size):
        if number_list[i] > number_list[j]:
            number_list[i], number_list[j] = number_list[j], number_list[i]
print("The list after sorting is: ")
for number in number_list:
    print(str(number), end=" ")
print("the 2nd largest number in the list is " + str(number_list[1]))