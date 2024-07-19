string = input("Enter the string to check if it is a palindrome: ")
string_length = len(string)
count = 0
for i in range(string_length // 2):
    if string[i] != string[-(i + 1)]:
        count += 1
if count == 0:
    print("Entered string is palindrome")
else:
    print("Entered string is not palindrome")
