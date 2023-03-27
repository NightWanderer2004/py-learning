# Write a function that takes a list of strings as an argument and returns a new list containing only the strings that start with a vowel.

def vowel_list(strings):
    vowels = "aeiou"
    new_strings = []
    for el in strings:
        if el[0] in vowels:
            new_strings.append(el)
    return new_strings


a = ["apple", "banana", "orange", "pear", "grape"]
print(vowel_list(a))
