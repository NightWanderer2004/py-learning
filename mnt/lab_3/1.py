import numpy as np

# Tworzenie macierzy A i wektora b
A = np.array([[10, 40, 70],
              [20, 50, 80],
              [30, 60, 80]], dtype=float)
b = np.array([300, 360, 390], dtype=float)

# Wyświetlenie macierzy początkowej
print("Macierz A:")
print(A)

# Metoda eliminacji Gaussa
n = len(A)
for j in range(n-1):
    # Obliczenie wyznacznika macierzy A
    dA = np.linalg.det(A)
    if dA != 0:
        # Tworzenie kopii macierzy A
        D = np.copy(A)
        for i in range(j+1, n):
            # Obliczenie współczynnika eliminacji
            factor = D[i, j] / D[j, j]
            # Eliminacja współczynników pod przekątną
            D[i, :] -= factor * D[j, :]
        # Przypisanie zmodyfikowanej macierzy D do macierzy A
        A = np.copy(D)

# Metoda Cramera
solutions = []
# Obliczenie wyznacznika macierzy A
dA = np.linalg.det(A)
if dA != 0:
    for j in range(n):
        # Tworzenie macierzy Dx na podstawie A i b
        Dx = np.copy(A)
        Dx[:, j] = b
        # Obliczenie wyznacznika macierzy Dx
        detD = np.linalg.det(Dx)
        # Obliczenie rozwiązania równania zgodnie z metodą Cramera
        x = detD / dA
        solutions.append(x)

# Sprawdzenie wyników
if len(solutions) == n:
    for i in range(n):
        print(f'x{i+1} = {solutions[i]}')
else:
    print('Układ równań jest sprzeczny lub nieoznaczony.')
