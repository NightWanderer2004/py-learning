# Napisz program, który prosi o podanie współczynników równania
# kwadratowego ax2 + bx + c = 0 i wypisuje rozwiązania równania(lub informację o braku rozwiązań)

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))

delta = b**2 - 4*a*c
s_delta = delta**0.5
x_1 = (-b + s_delta) / (2*a)
x_2 = (-b - s_delta) / (2*a)

print(
    f'Równanie: {a}x^2 + {b}x + {c} = 0\nWynik równania: x1 = {x_1}, x2 = {x_2}')
