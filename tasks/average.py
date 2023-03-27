# Write a function that takes a list of numbers as an argument and returns the average of all the numbers in the list.

def average(numbers):
    return sum(numbers) / len(numbers)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(average(a))
