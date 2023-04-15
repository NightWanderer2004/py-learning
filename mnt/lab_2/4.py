# Napisać program w języku Scilab ** (Python)**, który przy pomocy metody Newtona wyznacza wartość pierwiastka funkcji(16) dla punktu początkowego x = 0.05, a następnie dla punktu x = 0.9.
# Dla danych przypadków przyjąć dokładność przybliżenia δ = 1e-5, porównać zbieżność metody dla podanych punktów początkowych. y(x) = e^(5x)/100 - 1/4
# importujemy biblioteki
import numpy as np
import matplotlib.pyplot as plt


# definujemy funkcję
def funkcja(x):
    return (np.exp(5*x)/100) - 1/4


# pochodna funkcji
def pochodna(x):
    return 5*np.exp(5*x)/100


# metoda Newtona-Raphsona
def metoda_newtona(x0, delta):
    iteracje = 0
    x = x0
    # warunek kończący iteracje, jeśli znaleziono pierwiastek z dostatecznie małą dokładnością
    while abs(funkcja(x)) > delta:
        x = x - funkcja(x) / pochodna(x)
        iteracje += 1
    pierwiastek = x
    return pierwiastek, iteracje  # zwracamy znaleziony pierwiastek i liczbę iteracji


# definujemy zmienne
x0_1 = 0.05  # punkt startowy algorytmu
x0_2 = 0.9  # punkt startowy algorytmu
delta = 1e-5

# wywołujemy funkcję
pierwiastek_1, iteracje_1 = metoda_newtona(x0_1, delta)
pierwiastek_2, iteracje_2 = metoda_newtona(x0_2, delta)

# wykres funkcji
x = np.linspace(-1, 1, 1000)
y = funkcja(x)
fig, ax = plt.subplots()
ax.plot(x, y)
ax.axhline(y=0, color='black')
ax.axvline(x=0, color='black')

# oznaczamy punkty startowe i pierwiastki
ax.plot(x0_1, funkcja(x0_1), 'bo', label='x0 = 0.05')
ax.plot(x0_2, funkcja(x0_2), 'go', label='x0 = 0.9')
ax.plot(pierwiastek_1, 0, 'ro', label='pierwiastek 1')
ax.plot(pierwiastek_2, 0, 'mo', label='pierwiastek 2')
ax.legend()

plt.show()

# wyswietlamy wyniki
print("Dla x0 = 0.05:")
print("Pierwiastek: ", round(pierwiastek_1, 2))
print("Liczba iteracji: ", iteracje_1)

print("Dla x0 = 0.9:")
print("Pierwiastek: ", round(pierwiastek_2, 2))
print("Liczba iteracji: ", iteracje_2)
