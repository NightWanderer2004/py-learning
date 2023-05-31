# *Gauss*

'''import numpy as np


def gauss_elimination(A, B):
    n = len(A)

    # Etap eliminacji
    for i in range(n):
        # Znajdź największy element w kolumnie i zamień wiersze
        max_idx = i
        for j in range(i+1, n):
            if abs(A[j][i]) > abs(A[max_idx][i]):
                max_idx = j
        A[[i, max_idx]] = A[[max_idx, i]]
        B[[i, max_idx]] = B[[max_idx, i]]

        # Eliminacja współczynników pod przekątną
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            A[j] -= factor * A[i]
            B[j] -= factor * B[i]

    # Etap substitucji wstecznej
    X = np.zeros(n)
    for i in range(n-1, -1, -1):
        X[i] = (B[i] - np.dot(A[i][i+1:], X[i+1:])) / A[i][i]

    return X


# Współczynniki równań
A = np.array([[3, -4, 4, -4],
              [1.5, -1, 2, -2],
              [1.5, -0.5, 0, -3],
              [4.5, -5.5, 4, -9]])

# Wyrazy wolne
B = np.array([-9, -3.5, -2, -14])

# Rozwiązanie układu równań
X = gauss_elimination(A, B)

print("Rozwiązanie:")
for i in range(len(X)):
    print(f"x{i+1} =", X[i])'''


# *Cramer*

# importujemy bibliotekę numpy
import numpy as np

# definiujemy funkcję rozwiązującą układ równań metodą Cramera


def cramer_method(A, B):
    n = len(A)  # pobieramy rozmiar macierzy A

    det_A = np.linalg.det(A)  # obliczamy wyznacznik macierzy A

    # sprawdzamy, czy wyznacznik jest różny od zera
    if abs(det_A) < 1e-10:
        raise ValueError(
            "Układ równań ma nieskończenie wiele rozwiązań lub jest sprzeczny.")

    # jeśli wyznacznik jest różny od zera, to obliczamy rozwiązania
    X = np.zeros(n)

    # obliczamy rozwiązania
    for i in range(n):
        A_i = A.copy()  # Stworzenie kopii macierzy A
        A_i[:, i] = B   # Podmiana i-tej kolumny macierzy A na wektor wyrazów wolnych
        det_A_i = np.linalg.det(A_i)  # Obliczenie wyznacznika macierzy A_i
        X[i] = det_A_i / det_A  # Obliczenie i-tego rozwiązania

    return X


# Współczynniki równań
A = np.array([[3, -4, 4, -4],
              [1.5, -1, 2, -2],
              [1.5, -0.5, 0, -3],
              [4.5, -5.5, 4, -9]])

# Wyrazy wolne
B = np.array([-9, -3.5, -2, -14])

# Rozwiązanie układu równań
X = cramer_method(A, B)

# Wyświetlenie rozwiązania
print("Rozwiązanie:")
for i in range(len(X)):
    print(f"x{i+1} =", X[i])
