# Write a function that takes a list of strings as an argument and returns a new list containing all the strings in the list, but with the first letter of each string capitalized.

def capitalize_all(strings):
    return [el.capitalize() for el in strings]


a = ['hello', 'world', 'this', 'is', 'a', 'list', 'of', 'strings']
print(' '.join(capitalize_all(a)))
