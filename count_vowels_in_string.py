string = input("Enter the string: ").lower()
string_length = len(string)
count = 0
for i in range(string_length):
    if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u':
        count += 1

if count > 0:
    print("the number of vowels in the entered string is " + str(count))
else:
    print("there are no vowels in the entered string")
