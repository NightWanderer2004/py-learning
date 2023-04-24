# Utwórz macierz o wymiarach podanych przez użytkownika n × m wypełnioną losowymi liczbami całkowitymi z przedziału [0,9].

import random

n = int(input("Podaj n: "))
m = int(input("Podaj m: "))


def make_matrix(n, m):
    matrix = [[random.randint(0, 9) for i in range(m)] for j in range(n)]
    return matrix


matrix = make_matrix(n, m)
print("Matrix: ", matrix)
