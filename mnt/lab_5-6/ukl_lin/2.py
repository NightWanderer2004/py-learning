import numpy as np

# Wprowadź macierz współczynników układu równań
A = np.array([[4, -2, 1],
              [-2, 4, -2],
              [1, -2, 4]])

# Wprowadź wektor wyrazów wolnych
B = np.array([11, -16, 17])

# Połącz macierz A i wektor B w jedną macierz rozszerzoną
AB = np.column_stack((A, B)).astype(float)  # Dodaj .astype(float) tutaj

# Oblicz rozmiar macierzy A
n = len(A)

# Wykonaj eliminację Gaussa
for i in range(n):
    # Wybierz element diagonalny jako punkt odniesienia
    pivot = AB[i, i]

    # Skaluj wiersz, aby zapewnić wartość elementu diagonalnego równą 1
    AB[i, :] /= pivot

    # Wykonaj eliminację dla pozostałych wierszy
    for j in range(n):
        if i != j:
            factor = AB[j, i]
            AB[j, :] -= factor * AB[i, :]

# Wyodrębnij wektor rozwiązań
X = AB[:, -1]

# Wyświetl rozwiązania
for i, sol in enumerate(X):
    print(f"x{i+1} = {sol}")