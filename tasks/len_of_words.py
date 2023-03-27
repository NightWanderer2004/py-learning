# Write a function that takes a list of strings as an argument and returns a new list containing the length of each string.

def len_of_words(strings):
    return [len(el) for el in strings]


a = ["apple", "banana", "orange", "pear", "grape"]
print(len_of_words(a))
