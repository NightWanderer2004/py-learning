# Sprawdzić działanie metody Newtona dla poniższych funkcji: y(x) = x^5 − x + 1 i y(x) = e^x + 2x + 1

# importujemy biblioteki
import numpy as np

# metoda Newtona-Raphsona


def newton_method(f, df, x0, delta, max_iterations):
    x = x0
    for i in range(max_iterations):
        fx = f(x)

        if abs(fx) < delta:  # warunek kończący iteracje, jeśli znaleziono pierwiastek z dostatecznie małą dokładnością
            return x

        dfx = df(x)
        if dfx == 0:  # warunek kończący iteracje, jeśli pochodna jest równa zero
            break

        x = x - fx / dfx  # krok iteracyjny
    return x


# definujemy funkcji i ich pochodne
def f1(x):
    return x**5 - x + 1


def f1_derivative(x):
    return 5*x**4 - 1


def f2(x):
    return np.exp(x) + 2*x + 1


def f2_derivative(x):
    return np.exp(x) + 2


# funkcja pomocnicza do wyświetlania wyników
def print_result(x, f):
    print(f"Pierwiastek: x = {x:.8f}")
    print(f"Wartość funkcji: y = {f(x):.8f}")


# defingujemy zmienne
delta = 1e-6
x0 = 0.5  # punkt startowy algorytmu
max_iterations = 100  # maksymalna liczba iteracji

# wywołujemy funkcję i wyświetlamy wyniki
x = newton_method(f1, f1_derivative, x0, delta, max_iterations)
print("Funkcja y(x) = x^5 - x + 1:")
print_result(x, f1)
print()

x0 = -2.0
x = newton_method(f2, f2_derivative, x0, delta, max_iterations)
print("Funkcja y(x) = e^x + 2x + 1:")
print_result(x, f2)
