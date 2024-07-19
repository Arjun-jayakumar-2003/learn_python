before_encryption = input("enter the string to encrypt: ").lower()
shifter = int(input("Enter the shift key value: "))
ascii_values = [ord(char) for char in before_encryption]
length = len(before_encryption)
for i in range(0, length):
    ascii_values[i] += shifter
    if ascii_values[i] > 122:
        ascii_values[i] -= 26
after_encryption = "".join(chr(code) for code in ascii_values)
print("the encrypted string is " + after_encryption)
