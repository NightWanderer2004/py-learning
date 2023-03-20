# Napisz program, który oblicza pole i obwód koła o promieniu podanym przez użytkownika.
# Wartość stałej π weź z biblioteki math. Promień nie może być ujemny. W przypadku podania
# liczby ujemnej, program powinien wypisywać komunikat informujący o błędnej wartości i nic nie liczyć.

from math import pi


def circle_area(radius):
    resArea = pi * radius ** 2
    return round(resArea, 1)


def circle_circuit(radius):
    resCircuit = 2 * pi * radius
    return round(resCircuit, 1)


def main():
    radius = float(input("Podaj promień koła: "))
    if radius < 0:
        print("Promień nie może być ujemny!")
    else:
        print("Pole koła o promieniu", radius, "wynosi", circle_area(radius))
        print("Obwód koła o promieniu", radius,
              "wynosi", circle_circuit(radius))
main()
