import numpy as np

# Tworzenie macierzy A i wektora b
A = np.array([[10, 40, 70],
              [20, 50, 80],
              [30, 60, 80]])
b = np.array([300, 360, 390])

n = len(b)

# Eliminacja Gaussa
for k in range(n-1):
    # Dla każdej kolumny poniżej przekątnej macierzy A
    for i in range(k+1, n):
        # Obliczenie współczynnika eliminacji
        y = A[i, k] / A[k, k]
        # Modyfikacja wiersza i-tego macierzy A i wektora b
        for j in range(k+1, n):
            A[i, j] = A[i, j] - y * A[k, j]
        b[i] = b[i] - y * b[k]

# Rozwiązanie układu równań
x = np.zeros(n)
for i in range(n-1, -1, -1):
    S = 0
    for j in range(i+1, n):
        S = S + A[i, j] * x[j]
    x[i] = (b[i] - S) / A[i, i]

# Wyświetlenie wyniku
print("x1 =", x[0])
print("x2 =", x[1])
print("x3 =", x[2])
