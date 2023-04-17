# Napisz program, który:
# a) zsumuje wszystkie elementy macierzy;
# b) znajdzie element maksymalny macierzy oraz poda jego pozycję (indeks listy dwuwymiarowej);
# c) obliczy sumę wartości obydwóch przekątnych macierzy.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# a)
def sum_matrix(matrix):
    return sum([sum(i) for i in matrix])


print("a) ", sum_matrix(matrix))


# b)
def max_of_matrix(matrix):
    return max([max(i) for i in matrix])


print("b) ", max_of_matrix(matrix))


# c)
def sum_diagonal(matrix):
    sum = 0
    for i in range(len(matrix)):
        sum += matrix[i][i] + matrix[i][len(matrix)-i-1]
    return sum


print("c) ", sum_diagonal(matrix))


# ---NumPy version---
"""
import numpy as np

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# a)


def sum_matrix(matrix):
    arr = np.array(matrix)
    return np.sum(arr)


print("a) ", sum_matrix(matrix))

# b)


def max_of_matrix(matrix):
    arr = np.array(matrix)
    max_val = np.max(arr)
    max_index = np.where(arr == max_val)
    return max_val, max_index


print("b) ", max_of_matrix(matrix))

# c)


def sum_diagonal(matrix):
    arr = np.array(matrix)
    diagonal1 = np.diagonal(arr)
    diagonal2 = np.diagonal(np.fliplr(arr))
    diagonal_sum = np.sum(diagonal1) + np.sum(diagonal2)
    return diagonal_sum


print("c) ", sum_diagonal(matrix))
"""
