# Porównać zbieżność metod: bisekcji, siecznych oraz Newtona dla funkcji (10) i (11). Dla metod: bisekcji oraz siecznych, przyjąć przedział izolacji x ∈ [0.05, 1]. Dla metody Newtona przyjąć punkt początkowy x = 0.85. Przyjąć dokładność przybliżenia rozwiązania δ = 1e−6.

# definujemy funkcje przykladowe
def func10(x):
    return -x**2 + x - (1/5)


def func11(x):
    return -x**2 + x - 1


# definujemy metody obliczania pierwiastkow
def bisect(f, a, b, eps):
    # sprawdzamy czy funkcja ma znaki rozne na koncach przedzialu
    if f(a) * f(b) > 0:
        return None

    # wykonujemy petle dopoki nie osiagniemy zadanej dokladnosci
    while b - a > eps:
        x = (a + b) / 2
        if f(x) == 0:
            return x
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x

    # zwrocenie sredniej z koncow przedzialu
    return (a + b) / 2


def secant(f, x0, x1, eps):
    # wykonujemy petle dopoki nie osiagniemy zadanej dokladnosci
    while abs(x1 - x0) > eps:
        # wzor na metode siecznych
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0 = x1
        x1 = x2
    return x1


def newton(f, x0, eps):
    # wykonujemy petle dopoki nie osiagniemy zadanej dokladnosci
    while abs(f(x0)) > eps:
        x0 = x0 - f(x0) / (f(x0 + eps) - f(x0)) * \
            eps  # wzor na metode Newtona-Raphsona
    return x0


# definujemy przedzialy i dokladnosc
a = 0.05
b = 1
c = 0.85
delta = 1e-6

# wyswietlamy wyniki
print("Pierwiastek funkcji 10 metodą bisekcji: ", bisect(func10, a, b, delta))
print("Pierwiastek funkcji 11 metodą bisekcji: ", bisect(func11, a, b, delta))
print("Pierwiastek funkcji 10 metodą siecznych: ", secant(func10, a, b, delta))
print("Pierwiastek funkcji 11 metodą siecznych: ", secant(func11, a, b, delta))
print("Pierwiastek funkcji 10 metodą Newtona-Raphsona: ", newton(func10, c, delta))
print("Pierwiastek funkcji 11 metodą Newtona-Raphsona: ", newton(func11, c, delta))
