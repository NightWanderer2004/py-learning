import numpy as np             # Importujemy bibliotekę NumPy do operacji na liczbach i tablicach
import matplotlib.pyplot as plt  # Importujemy bibliotekę Matplotlib do tworzenia wykresów

def f(x):                      # Definiujemy funkcję, której pierwiastek będziemy szukać
    return x**2 + x - 1

t = np.arange(-1, 1, 0.01)     # Tworzymy tablicę t, w której przechowujemy wartości od -1 do 1 z krokiem 0.01

plt.plot(t, f(t))              # Rysujemy wykres funkcji f(x) na przedziale [-1, 1]
plt.grid(True)                 # Włączamy siatkę na wykresie
plt.xlabel('$x$')              # Dodajemy etykietę osi x
plt.ylabel('$y(x)$')           # Dodajemy etykietę osi y

a = t[0]                       # Ustawiamy początkową wartość przedziału poszukiwania
b = t[-1]                      # Ustawiamy końcową wartość przedziału poszukiwania
e = 1e-4                       # Ustawiamy dokładność, z jaką chcemy znaleźć pierwiastek
iMax = 100                     # Ustawiamy maksymalną liczbę iteracji

for k in range(iMax):          # Uruchamiamy pętlę, która będzie szukać pierwiastka w danym przedziale
    x = (a + b) / 2            # Obliczamy środek przedziału
    if abs(f(x)) < e:         # Jeśli wartość funkcji w punkcie x jest dostatecznie bliska zeru, to znaleźliśmy pierwiastek
        yo = f(x)             # Zapisujemy wartość funkcji w punkcie x jako yo
        xo = x                # Zapisujemy wartość x jako xo
        break                 # Przerywamy pętlę
    elif f(a) * f(x) < 0:     # Jeśli wartości funkcji w punktach a i x mają różne znaki, to pierwiastek znajduje się w przedziale [a, x]
        b = x                 # Ustawiamy końcową wartość przedziału jako x
    else:                     # W przeciwnym przypadku pierwiastek znajduje się w przedziale [x, b]
        a = x                 # Ustawiamy początkową wartość przedziału jako x

plt.plot(xo, yo, 'ro')        # Rysujemy punkt na wykresie, który odpowiada znalezionemu pierwiastkowi

plt.show()                     # Wyświetlamy wykres
