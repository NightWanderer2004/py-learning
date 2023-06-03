import numpy as np
import matplotlib.pyplot as plt

# Dane wejściowe
t = np.array([0.000, 0.698, 1.396, 2.094, 3.490, 4.188, 4.886, 5.585, 6.283])
y = np.array([2.353, 2.043, 1.713, 1.517, 1.788, 2.129, 2.409, 2.498, 2.353])

# Wykres punktowy
plt.scatter(t, y, color='blue', label='Dane')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Wykres danych')

# Aproksymacja funkcji
A = np.vstack([np.ones(len(t)), np.cos(t), np.sin(t)]).T
coefficients, residuals, _, _ = np.linalg.lstsq(A, y, rcond=None)

A0 = coefficients[0]
A1 = coefficients[1]
B1 = coefficients[2]

# Wyliczanie amplitudy
C = np.sqrt(A1**2 + B1**2)

# Wyliczanie kąta przesunięcia fazowego
if A1 < 0:
    theta = np.arctan(-B1 / A1) + np.pi
else:
    theta = np.arctan(-B1 / A1)


# Funkcja aproksymująca
def f(t): return A0 + A1 * np.cos(t) + B1 * np.sin(t)


# Linia funkcji aproksymującej
t_line = np.linspace(0, 2 * np.pi, 100)
y_line = f(t_line)
plt.plot(t_line, y_line, color='red',
         label='f(t) = A0 + A1*cos(t) + B1*sin(t)')

plt.legend()
plt.grid(True)
plt.show()

# Wyświetlanie wyników
print("Wartość średnia A0:", A0)
print("Amplituda C:", C)
print("Kąt przesunięcia fazowego θ:", theta)
