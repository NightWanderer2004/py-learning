# Wygenerować wykres funkcji: y1(t) = sin(t) * e^-0,08t, gdzie t ∈< 0, 12 > z krokiem równym 0, 01

# importujemy moduł NumPy i matplotlib
from numpy import *
from matplotlib.pylab import *


# definujemy funkcję y1(t)
def y1(t):
    return sin(t) * exp(-0.08 * t)  # zwracamy wartość funkcji


t = np.arange(0, 12, 0.01)  # generujemy wektor "t" od 0 do 20 z krokiem 0.2
y = y1(t)  # obliczamy wartości funkcji y1(t)

# narysowanie wykresu i ustanowienie parametrów
plot(t, y)
xlabel('t')
ylabel('y1(t)')

title('Wykres funkcji y1(t) = sin(t) * e^-0,08t')  # dodajemy tytuł wykresu
legend(('y1(t)'))  # dodajemy legendę

grid(True)  # włączamy siatkę pomocniczą
show()  # wyświetlamy wykres
