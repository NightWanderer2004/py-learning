# Napisz program, który prosi o podanie współczynników równania
# kwadratowego ax2 + bx + c = 0 i wypisuje rozwiązania równania(lub informację o braku rozwiązań)

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
c = int(input("Podaj c: "))


def calc_delta(a, b, c):
    return b**2 - 4*a*c


def calc_square_root(delta):
    return delta**0.5


def calc_x(pos, a, b, s_delta):
    if pos == 1:
        return (-b + s_delta) / (2*a)
    elif pos == 2:
        return (-b + s_delta) / (2*a)


delta = calc_delta(a, b, c)
s_delta = calc_square_root(delta)

x_1 = (calc_x(1, a, b, s_delta))
x_2 = (calc_x(2, a, b, s_delta))

print(
    f'Równanie: {a}x^2 + {b}x + {c} = 0\nWynik równania: x1 = {x_1}, x2 = {x_2}')
