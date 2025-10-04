string = input("Enter a string to reverse: ")

#print(f"Reversed string is:  {string[::-1]}")  # Slicing method Pythonic way

reversed_string = ""
for char in string:
    reversed_string = char + reversed_string  # Prepend each character to build the reversed string
print(f"Reversed string is:  {reversed_string}")