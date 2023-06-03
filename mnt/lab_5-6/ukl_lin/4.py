import numpy as np

# Funkcja do obliczania optymalnej wartości współczynnika relaksacji
def calculate_optimal_relaxation(xk, xkp, k, p):
    norm_diff = np.linalg.norm(xkp, ord=2) / (np.linalg.norm(xk, ord=2) + 1e-10)  # Dodajemy 1e-10, aby uniknąć dzielenia przez zero
    value = 1 - (norm_diff ** (1 / p))
    if value >= 0:
        lambda_opt = 2 / (1 + np.sqrt(value))
    else:
        lambda_opt = 2 / (1 + np.sqrt(1e-10))
    return lambda_opt

# Układ równań
A = np.array([[4, 2, 4, 5, 8],
              [2, 10, 2, 6, 9],
              [8, 2, 12, 1, 2],
              [8, 6, 1, 13, 8],
              [9, 2, -2, 5, 8]])
b = np.array([1, 5, 2, 8, 4])

# Parametry
k = 5
p = 2

# Początkowe wartości wektora x
xk = np.zeros_like(b)

# Iteracja
for iteration in range(k):
    # Obliczanie nowego przybliżenia x
    xkp = np.copy(xk)
    for i in range(len(b)):
        xkp[i] = (b[i] - np.dot(A[i, :i], xkp[:i]) - np.dot(A[i, i + 1:], xk[i + 1:])) / A[i, i]
    
    # Obliczanie optymalnego współczynnika relaksacji
    lambda_opt = calculate_optimal_relaxation(xk, xkp, k, p)
    
    # Aktualizacja wartości wektora x
    xk = (1 - lambda_opt) * xk + lambda_opt * xkp

# Wynik
print("Optymalna wartość współczynnika relaksacji:", lambda_opt)
print("Rozwiązanie układu równań:")
print("x1 =", xk[0])
print("x2 =", xk[1])
print("x3 =", xk[2])
print("x4 =", xk[3])
print("x5 =", xk[4])