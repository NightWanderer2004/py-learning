import numpy as np

# Definicja macierzy A i wektora prawych stron b
A = np.array([[10, 40, 70],
              [20, 50, 80],
              [30, 60, 80]])
b = np.array([300, 360, 390])

# Wyświetlenie wartości początkowej macierzy A
print("Macierz A:")
print(A)

# Sprawdzenie, czy macierz A jest osobliwa
det_A = np.linalg.det(A)
if det_A == 0:
    print("Macierz A jest osobliwa. Nie można rozwiązać układu równań.")
else:
    # Rozwiązanie układu równań metodą eliminacji Gaussa
    x = np.zeros(len(b))
    for k in range(len(b)-1):
        for i in range(k+1, len(b)):
            y = A[i, k] / A[k, k]
            for j in range(k+1, len(b)):
                A[i, j] = A[i, j] - y * A[k, j]
            b[i] = b[i] - y * b[k]
    for i in range(len(b)-1, -1, -1):
        S = 0
        for j in range(i+1, len(b)):
            S = S + A[i, j] * x[j]
        x[i] = (b[i] - S) / A[i, i]

    # Wyświetlenie wyniku
    print("Rozwiązanie:")
    print(f"x1 = {x[0]}, x2 = {x[1]}, x3 = {x[2]}")
