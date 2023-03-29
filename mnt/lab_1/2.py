# Zapoznać się z modułem NumPy. Uruchomić i zmodyfikować przykłady z instrukcji.

import numpy as np  # importujemy moduł NumPy

# tworzymy macierz 2x2 za pomocą "array"
A = np.array([[1, 2], [3, 4]])
B = np.array([[1, 1], [2, 2]])

# mnożenie macierzy = array ([[1 , 2], [6, 8]])
print("mnożenie macierzy (A * B): ", A * B)

# mnożenie macierzy = array ([[5 , 5], [11, 11]])
print("mnożenie macierzy: (dot)", np.dot(A, B))

# tworzymy macierz 2x2 za pomocą "matrix"
A = np.matrix([[1, 2], [3, 4]])
B = np.matrix([[1, 1], [2, 2]])

# mnożenie macierzy = matrix ([[5 , 5], [11, 11]])
print("mnożenie macierzy (A * B): ", A * B)

# mnożenie macierzy = matrix ([[1 , 2], [6, 8]])
print("mnożenie macierzy: (multiply): ", np.multiply(A, B))
# wypisuje element w wierszu 0 i kolumnie 0 = 1
print("pierwszy element pierwszego rządu: ", A[0, 0])
