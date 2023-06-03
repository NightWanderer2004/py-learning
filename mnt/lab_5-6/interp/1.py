import numpy as np
import matplotlib.pyplot as plt

# Węzły interpolacji
x = np.array([2, 2.5, 4]) # Ustawienie wartości węzłów interpolacji
y = 1 / x # Obliczenie wartości funkcji dla każdego węzła

# Wielomian interpolacyjny
coefficients = np.polyfit(x, y, 2) # Obliczenie współczynników wielomianu interpolacyjnego
poly = np.poly1d(coefficients) # Utworzenie wielomianu interpolacyjnego na podstawie obliczonych współczynników

# Punkty do wykresu
x_plot = np.linspace(1.5, 4.5, 100) # Ustawienie przedziału, dla którego mają być wyznaczone wartości wielomianu
y_plot = poly(x_plot) # Obliczenie wartości wielomianu interpolacyjnego dla punktów z przedziału x_plot

# Wykres
plt.plot(x, y, 'ro', label='Węzły interpolacji') # Wykres punktów interpolacji
plt.plot(x_plot, y_plot, label='Wielomian interpolacyjny') # Wykres wielomianu interpolacyjnego
plt.xlabel('x') # Etykieta osi x
plt.ylabel('f(x)') # Etykieta osi y
plt.legend() # Dodanie legendy
plt.title('Wielomian interpolacyjny n = 2 dla f(x) = 1/x') # Tytuł wykresu
plt.grid(True) # Dodanie siatki
plt.show() # Wyświetlenie wykresu