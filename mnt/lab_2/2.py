# Zmodyfikuj program z zadania 1, tak aby wyznaczał wartość pierwiastka funkcji: y(x) = -x^2 + x - (1/5)

# imortujemy biblioteki
import numpy as np
import matplotlib.pyplot as plt


# definiujemy funkcję f(x)
def f(x):
    return -x**2 + x - (1/5)


# tworzymy tablicę wartości argumentu funkcji od -1 do 1 z krokiem 0.01
t = np.arange(0, 1, 0.01)

# rysujemy wykres funkcji
plt.plot(t, f(t))

# dodajemy siatkę i etykiety osi
plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('$y(x)$')

# definujemy początkowe wartości przedziału, w którym szukamy pierwiastka
a = t[0]  # lewa granica przedziału
b = t[-1]  # prawa granica przedziału
e = 1e-4
iMax = 100

# używamy metody bisekcji do znalezienia pierwiastka równania
y = 0
for k in range(iMax):
    x = (a + b) / 2
    if abs(f(x)) < e:
        y = f(x)
        break
    elif f(a) * f(x) < 0:
        b = x
    else:
        a = x

# wyświetlamy znaleziony pierwiastek na wykresie
plt.plot(x, y, 'ro')
plt.show()
