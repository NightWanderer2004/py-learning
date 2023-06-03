# Importowanie bibliotek
import numpy as np


# Funkcja aproksymowana
def y(x):
    return np.sin(x)


# Przedział x
x = np.arange(-np.pi, np.pi, np.pi/30)

# Stopnie wielomianów aproksymujących
degrees = [1, 2, 3, 5]

# Obliczanie błędów aproksymacji dla różnych stopni wielomianów
errors = []
for degree in degrees:
    coefficients = np.polyfit(x, y(x), deg=degree)
    g = np.polyval(coefficients, x)
    error = np.sum((y(x) - g)**2)
    errors.append(error)

# Wyświetlanie wyników
print("Błędy aproksymacji:")
for i, degree in enumerate(degrees):
    print(f"Wielomian stopnia {degree}): {errors[i]}")
