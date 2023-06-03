import numpy as np
import matplotlib.pyplot as plt

# Funkcja f(x)
def f(x):
    return 1 / (x**3 + 1)

# Węzły interpolacji
x_interpolation = [1, 2, 4, 8, 16] # Ustawienie wartości węzłów interpolacji
y_interpolation = [f(x) for x in x_interpolation] # Obliczenie wartości funkcji dla każdego węzła

# Wielomian interpolacyjny
coefficients = np.polyfit(x_interpolation, y_interpolation, len(x_interpolation) - 1) # Obliczenie współczynników wielomianu interpolacyjnego
poly = np.poly1d(coefficients) # Utworzenie wielomianu interpolacyjnego na podstawie obliczonych współczynników

# Punkty do wykresu funkcji f(x)
x_plot = np.linspace(0.5, 16.5, 500) # Ustawienie przedziału, dla którego mają być wyznaczone wartości funkcji f(x)
y_plot = f(x_plot) # Obliczenie wartości funkcji f(x) dla punktów z przedziału x_plot

# Punkty do wykresu wielomianu interpolacyjnego P(x)
y_interpolation_poly = poly(x_plot) # Obliczenie wartości wielomianu interpolacyjnego dla punktów z przedziału x_plot

# Wykres
plt.plot(x_interpolation, y_interpolation, 'ro', label='Węzły interpolacji') # Wykres punktów interpolacji
plt.plot(x_plot, y_plot, label='f(x)') # Wykres funkcji f(x)
plt.plot(x_plot, y_interpolation_poly, label='P(x)') # Wykres wielomianu interpolacyjnego P(x)
plt.xlabel('x') # Etykieta osi x
plt.ylabel('y') # Etykieta osi y
plt.legend() # Dodanie legendy
plt.title('Interpolacja funkcji f(x)') # Tytuł wykresu
plt.grid(True) # Dodanie siatki
plt.show() # Wyświetlenie wykresu
