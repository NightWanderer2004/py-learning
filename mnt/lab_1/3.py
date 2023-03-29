# Zapoznać się z biblioteką Matplotlib. Uruchomić przykłady z instrukcji. Utworzyć własne wykresy.

# importujemy moduł NumPy i matplotlib
from numpy import *
from matplotlib.pylab import *

x = arange(0, 100, 0.1)  # generujemy wektor x od 0 do 10 z krokiem 0.1
sin_line = sin(5 * pi * x / 255)  # definujemy funkcję sinus
cos_line = cos(5 * pi * x / 255)  # definujemy funkcję cosinus

# narysowanie wykresu i ustanowienie parametrów
plot(x, sin_line, linewidth=3.0)
plot(x, cos_line, linewidth=6.0)

# dodajemy etykiety osi
xlabel('x')
ylabel('y')

# dodajemy tytuły wykresu
title('Wykres funkcji sinus i cosinus')
legend(('sin(x)', 'cos(x)'))

grid(True)  # włączamy siatkę pomocniczą
show()  # wyświetlamy wykres
