# Write a function that takes a string as an argument and returns a list of all the words in the string.

def split_string(string):
    return string.split()


test_string = split_string("Hello world!")

for word in test_string:
    print(word)
