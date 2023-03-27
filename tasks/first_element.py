# Write a function that takes a list of tuples as an argument and returns a new list containing the first element of each tuple.

def first_element(tuples):
    return [el[0] for el in tuples]


a = [(1, 2), (3, 4), (5, 6)]
print(first_element(a))
