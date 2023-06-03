# Importowanie bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Dane wejściowe
x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
y = np.array([2.1, 7.7, 13.6, 27.2, 40.9, 61.1])

# Macierz A
A = np.vstack([np.ones(len(x)), x, x**2]).T

# Obliczanie współczynników a0, a1, a2 dla g(x) = a0 + a1*x + a2*x^2
coefficients1, residuals1, _, _ = np.linalg.lstsq(A, y, rcond=None)

# Funkcja aproksymująca g1(x) = a0 + a1*x + a2*x^2
# Odwrócenie kolejności współczynników dla np.poly1d
g1 = np.poly1d(coefficients1[::-1])

# Obliczanie współczynników a0, a1 dla g(x) = a0 + a1*x
coefficients2, residuals2, _, _ = np.linalg.lstsq(A[:, :-1], y, rcond=None)

# Funkcja aproksymująca g2(x) = a0 + a1*x
# Odwrócenie kolejności współczynników dla np.poly1d
g2 = np.poly1d(coefficients2[::-1])

# Wykresy
plt.scatter(x, y, color='blue', label='Dane')  # Punkty danych
plt.plot(x, g1(x), color='red', label='g(x) = a0 + a1*x + a2*x^2')  # Wykres g1(x)
plt.plot(x, g2(x), color='green', label='g(x) = a0 + a1*x')  # Wykres g2(x)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Aproksymacja funkcji')
plt.legend()
plt.grid(True)
plt.show()
