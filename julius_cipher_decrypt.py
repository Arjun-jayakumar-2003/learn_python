before_decryption = input("enter the string to decrypt: ").lower()
shifter = int(input("Enter the shift key value: "))
ascii_values = [ord(char) for char in before_decryption]
length = len(before_decryption)
for i in range(0, length):
    ascii_values[i] -= shifter
    if ascii_values[i] < 97:
        ascii_values[i] += 26
after_decryption = "".join(chr(code) for code in ascii_values)
print("the decrypted string is " + after_decryption)
