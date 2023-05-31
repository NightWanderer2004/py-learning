import numpy as np

# Macierz współczynników
A = np.array([[10, 40, 70],
              [20, 50, 80],
              [30, 60, 80]], dtype=np.float64)

# Wektor wyrazów wolnych
b = np.array([300, 360, 390], dtype=np.float64)

# Połączenie macierzy A i b
AB = np.column_stack((A, b))

# Liczba równań
r = A.shape[0]

# Eliminacja Gaussa
for k in range(r - 1):
    for i in range(k + 1, r):
        # Obliczenie współczynnika eliminacji
        factor = AB[i, k] / AB[k, k]
        # Eliminacja współczynników pod przekątną
        AB[i, k:] -= factor * AB[k, k:]

# Wyliczanie rozwiązań
x = np.zeros(r)
for i in range(r - 1, -1, -1):
    x[i] = (AB[i, -1] - np.dot(AB[i, i + 1:-1], x[i + 1:])) / AB[i, i]

# Wyświetlanie rozwiązań
for i, sol in enumerate(x):
    print(f'x{i+1} = {sol}')
