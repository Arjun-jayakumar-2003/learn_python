string = input("Enter the string whose frequency count is to be found: ")

frequency_dictionary = {}

for char in string:
    if char in frequency_dictionary:
        frequency_dictionary[char] += 1
    else:
        frequency_dictionary[char] = 1

for char, frequency in frequency_dictionary.items():
    print(f"The frequency of {char} is {frequency}")
