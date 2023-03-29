# Utworzyć funkcję wyznaczającą wartość liczby π według zależności:
# SUM(inf, k=0) * ((-1^k) / (2k + 1)) = π/4

# definicja funkcji dla obliczenia liczby pi
def calculate_pi(n):
    pi = 0  # zmienna przechowująca wartość liczby pi
    for k in range(n):  # pętla for dla k od 0 do n
        pi += ((-1)**k) / (2*k + 1)  # obliczenie wartości liczby pi
    pi *= 4  # mnożenie przez 4
    return pi  # zwrócenie wartości liczby pi


w

# wywołanie funkcji z argumentem nieskończoności - wynik: 3.141592653589793
print(calculate_pi(1000000))
