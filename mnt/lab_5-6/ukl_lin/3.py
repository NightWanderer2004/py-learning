import numpy as np

# Przygotowanie macierzy współczynników
A = np.array([[14, 2, 4, 5, 8],
              [2, 10, 2, 6, 9],
              [8, 2, 12, 1, 2],
              [8, 6, 1, 13, 8],
              [9, 2, -2, 5, 8]], dtype=float)

# Przygotowanie wektora wynikowego
B = np.array([1, 5, 2, 8, 4], dtype=float)

# Połączenie macierzy A i B
AB = np.column_stack((A, B))

# Rozwiązanie układu równań za pomocą metody Gaussa
n = len(B)
for i in range(n):
    # Wybór elementu głównego (pivot)
    pivot = AB[i, i]
    if pivot == 0:
        raise ValueError("Błąd.")
        
    # Normalizacja wiersza
    AB[i, :] /= pivot

    # Eliminacja
    for j in range(i+1, n):
        ratio = AB[j, i] / AB[i, i]
        AB[j, :] -= ratio * AB[i, :]

# Rozwiązanie układu równań (back substitution)
x = np.zeros(n)
x[n-1] = AB[n-1, n]
for i in range(n-2, -1, -1):
    x[i] = AB[i, n] - np.dot(AB[i, i+1:n], x[i+1:n])

# Wyświetlenie wyników
print("Rozwiązanie:")
for i, value in enumerate(x):
    print("x{} = {}".format(i+1, value))