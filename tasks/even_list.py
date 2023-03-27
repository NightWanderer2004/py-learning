# Write a function that takes a list of numbers as an argument and returns a new list containing only the even numbers.

def even_list(numbers):
    return [el for el in numbers if el % 2 == 0]


a = [1, 2, 3, 4, 5]
print(even_list(a))
