# Write a function that takes a list of numbers as an argument and returns the sum of all the numbers in the list

def list_sum(numbers):
    sum_of_list = 0
    for el in numbers:
        sum_of_list += el
    return sum_of_list


a = [1, 2, 3, 4, 5]
print(list_sum(a))
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_sum(b))
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(list_sum(c))
