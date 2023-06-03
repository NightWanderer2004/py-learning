# Importowanie bibliotek
import numpy as np
import matplotlib.pyplot as plt

# Tworzenie danych punktowych
# Tworzenie tablicy x z wartościami od -π do π z krokiem π/30
x = np.arange(-np.pi, np.pi, np.pi/30)
y = np.sin(x)  # Obliczanie wartości funkcji y(x) = sin(x) dla każdego x

# Tworzenie macierzy A
# Tworzenie macierzy A, gdzie pierwsza kolumna to x^3, a druga kolumna to x
A = np.vstack([x**3, x]).T

# Obliczanie współczynników c1 i c2
# Obliczanie współczynników metodą najmniejszych kwadratów
coefficients, residuals, _, _ = np.linalg.lstsq(A, y, rcond=None)

c1 = coefficients[0]  # Pierwszy współczynnik to c1
c2 = coefficients[1]  # Drugi współczynnik to c2


# Obliczanie wartości funkcji aproksymującej
# Obliczanie wartości funkcji aproksymującej ya(x) = c1*x^3 + c2*x
def ya(x):
    return c1 * x**3 + c2 * x


# Obliczanie błędu aproksymacji
# Obliczanie sumy kwadratów różnic między wartościami y i ya
error = np.sum((y - ya(x))**2)

# Wyświetlanie wyników
print("Współczynniki:")
print("c1 =", c1)
print("c2 =", c2)
print("Błąd aproksymacji =", error)

# Wykres
# Wykres funkcji y(x) = sin(x)
plt.plot(x, y, label='y(x) = sin(x)', color='blue')
# Wykres funkcji aproksymującej ya(x) = c1*x^3 + c2*x
plt.plot(x, ya(x), label='ya(x) = c1*x^3 + c2*x', color='red')
plt.legend()  # Dodanie legendy do wykresu
plt.xlabel('x')  # Opis osi x
plt.ylabel('y')  # Opis osi y
plt.title('Aproksymacja funkcji y(x) za pomocą wielomianu')  # Tytuł wykresu
plt.grid(True)  # Włączenie siatki
plt.show()  # Wyświetlenie wykresu
