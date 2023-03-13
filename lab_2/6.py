# Napisz program proszący użytkownika o imię i rok urodzenia, a następnie obliczający i wypisujący jego wiek.

name = input("Enter your name:\n")
year = int(input("Enter your year of birth:\n"))


def get_age(year):
    return 2023 - year


print(" Name:", name, "\n", "Age in 2023:", get_age(year))
