# 5. Napisz program, który wylosuje dowolną liczbę całkowitą od zera do 10 (do losowania liczb użyj
# np. funkcji randint z biblioteki random https://docs.python.org/3/library/random.html), a następnie
# prosi użytkownika o jej zgadnięcie tak długo, aż ten poda poprawną wartość. Gdy program działa,
# rozszerz go o podawanie informacji za którym razem udało się zgadnąć oraz o wskazówki typu
# „Podana przez ciebie liczba jest większa/mniejsza od wylosowanej”.

import random

number = random.randint(0, 10)
guess = -1
guesses = 0


def check_input(guesses):
    user_inp = int(input("Zgadnij liczbę od 0 do 10: "))
    guesses += 1
    return user_inp


def check_correct(number, guess, guesses):
    if guess < number:
        print("Podana przez ciebie liczba jest za mała.")
    elif guess > number:
        print("Podana przez ciebie liczba jest za duża.")
    else:
        print("Gratulacje, zgadłeś liczbę!")
        print("Udało Ci się zgadnąć za", guesses, "razem.")


while guess != number:
    guess = check_input(guesses)
    check_correct(number, guess, guesses)
