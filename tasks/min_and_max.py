# Write a function that takes a list of integers as an argument and returns a tuple containing the minimum and maximum values in the list.

def min_and_max(numbers):
    return tuple((min(numbers), max(numbers)))


a = [1, 2, 3, 4, 5]
print(min_and_max(a))
