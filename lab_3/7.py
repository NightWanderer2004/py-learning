# Napisz program drukujący na ekranie prostokąt z literek X. Wysokość i szerokość prostokąta
# wczytujemy z klawiatury:
# XXXXXXXXXX
# X        X
# X        X
# X        X
# XXXXXXXXXX

height = int(input("Podaj wysokość prostokąta: "))
width = int(input("Podaj szerokość prostokąta: "))


def print_x(height, width, i, j):
    if i == 0 or i == height - 1 or j == 0 or j == width - 1:
        print("X", end="")
    else:
        print(" ", end="")


for i in range(height):
    for j in range(width):
        print_x(height, width, i, j)
    print()
