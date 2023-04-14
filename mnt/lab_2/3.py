# Napisz program w języku Python, który przy pomocy metody siecznych wyznaczy wartość pierwiastka następujących funkcji w przedziale izolacji[0.05, 1]

# importujemy bibliotekę numpy
import numpy as np


# definujemy 5 funkcijs
def func1(x):
    return x**2 + x - 1


def func2(x):
    return (np.exp(5*x) / 100) - 0.25


def func3(x):
    return -np.exp(-5*x) + 0.25


def func4(x):
    return np.exp(-5*x) - 0.25


def func5(x):
    return -(np.exp(5*x) / 100) + 0.5


# definujemy metodę siecznych
def secant_method(func, a, b, eps):
    # x0 i x1 to punkty początkowe
    x0 = a
    x1 = b

    # sprawdzamy czy funkcja przyjmuje wartości o różnych znakach
    while abs(x1 - x0) > eps:
        # wzór na metodę siecznych
        x2 = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))
        x0 = x1
        x1 = x2
    return x2


# definiujemy przedział
a = 0.05
b = 1
delta = 0.0001

# wyswietlamy wyniki
print("func1 root: ", secant_method(func1, a, b, delta))
print("func2 root: ", secant_method(func2, a, b, delta))
print("func3 root: ", secant_method(func3, a, b, delta))
print("func4 root: ", secant_method(func4, a, b, delta))
print("func5 root: ", secant_method(func5, a, b, delta))
