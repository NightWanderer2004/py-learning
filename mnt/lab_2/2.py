import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.where((0 <= x) & (x <= 1), -x**2 + np.where(x > 0, x**(-1/5), np.nan), np.nan)

# Tworzymy tablicę wartości argumentu funkcji od -1 do 1 z krokiem 0.01
t = np.arange(0, 1, 0.01)

# Rysujemy wykres funkcji
plt.plot(t, f(t))
plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('$y(x)$')

# Ustawiamy początkowe wartości do poszukiwania pierwiastka
a = t[0]  # lewa granica przedziału
b = t[-1]  # prawa granica przedziału
e = 1e-4  # dokładność poszukiwania
iMax = 100  # maksymalna liczba iteracji

# Używamy metody bisekcji do znalezienia pierwiastka równania
y = 0  # initialize y
for k in range(iMax):
    x = (a + b) / 2
    if abs(f(x)) < e:
        y = f(x)
        break
    elif f(a) * f(x) < 0:
        b = x
    else:
        a = x

# Wyświetlamy znaleziony pierwiastek na wykresie
plt.plot(x, y, 'ro')

# Wyświetlamy wykres funkcji i znalezionego pierwiastka
plt.show()
