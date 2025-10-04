#Count Vowels and Consonts in gien string

string = input("Enter String: ")
vowels = ["a","e","i","o","u"]
vowels_count = 0
consonants_count = 0

for char in string.lower():
    if char.isalpha():
        if char in vowels:
            vowels_count +=1
        else:
            consonants_count +=1

print(f"In given sting {string}, vowels = {vowels_count},consonants = {consonants_count}")