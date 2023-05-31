import numpy as np

# Definicja macierzy A i wektora prawych stron b
A = np.array([[0, 2, 2], [3, 3, 0], [1, 0, 1]])
b = np.array([1, 3, 2])

# Wyświetlenie wartości początkowej macierzy A
print("Macierz A:")
print(A)

# Sprawdzenie, czy macierz A jest osobliwa
det_A = np.linalg.det(A)
if det_A == 0:
    print("Macierz A jest osobliwa. Nie można rozwiązać układu równań.")
else:
    # Rozwiązanie układu równań metodą eliminacji Gaussa
    x = np.linalg.solve(A, b)
    x = np.round(x, 1)  # Zaokrąglenie wyników do jednego miejsca po przecinku
    print("\nRozwiązanie układu równań (metoda eliminacji Gaussa):")
    print(f"x1 = {x[0]}, x2 = {x[1]}, x3 = {x[2]}")

    # Porównanie wyników z metodą Cramera
    det_A1 = np.linalg.det(np.column_stack((b, A[:, 1:])))
    det_A2 = np.linalg.det(np.column_stack((A[:, 0], b, A[:, 2])))
    det_A3 = np.linalg.det(np.column_stack((A[:, :2], b)))

    x1 = det_A1 / det_A
    x2 = det_A2 / det_A
    x3 = det_A3 / det_A

    # Zaokrąglenie wyników do jednego miejsca po przecinku
    x1 = np.round(x1, 1)
    x2 = np.round(x2, 1)
    x3 = np.round(x3, 1)

    print("\nRozwiązanie układu równań (metoda Cramera):")
    print(f"x1 = {x1}, x2 = {x2}, x3 = {x3}")
