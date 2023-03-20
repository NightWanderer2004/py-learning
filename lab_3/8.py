# Napisz program drukujący na ekranie trójkąt z literek X.
# Wysokość trójkąta wczytujemy z klawiatury.

height = int(input("Podaj wysokość trójkąta: "))
for i in range(1, height + 1):
    print("X" * i)
