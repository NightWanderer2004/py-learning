# importujemy biblioteki
import numpy as np
import matplotlib.pyplot as plt


# definiujemy funkcję f(x)
def f(x):
    return x**2 + x - 1


# tworzymy tablicę t, w której przechowujemy wartości od -1 do 1 z krokiem 0.01
t = np.arange(-1, 1, 0.01)

# rysujemy wykres funkcji f(x) na przedziale [-1, 1]
plt.plot(t, f(t))

# dodajemy siatkę i etykiety osi
plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('$y(x)$')

# definujemy początkowe wartości przedziału, w którym szukamy pierwiastka
a = t[0]
b = t[-1]
e = 1e-4
iMax = 100

# uruchamiamy pętlę, która będzie szukać pierwiastka w danym przedziale
for k in range(iMax):
    # obliczamy środek przedziału
    x = (a + b) / 2

    # sprawdzamy, czy wartość funkcji w punkcie x jest dostatecznie bliska zeru
    if abs(f(x)) < e:
        yo = f(x)
        xo = x
        break
    # jeśli nie, to sprawdzamy, czy wartość funkcji w punkcie x jest mniejsza od zera
    elif f(a) * f(x) < 0:
        b = x
    else:
        a = x

# rysujemy punkt na wykresie, który odpowiada znalezionemu pierwiastkowi
plt.plot(xo, yo, 'ro')
plt.show()
