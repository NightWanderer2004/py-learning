# Napisz program grający z użytkownikiem w rzut monetą. Działanie programu powinno być zbliżone do następującego:
# użytkownik wybiera czy obstawia reszkę, czy orła(wykorzystaj wartości boolowskie)
# po dokonaniu wyboru, komputer odlicza(3, 2, 1 - wykorzystaj metodę sleep() biblioteki time), a następnie dokonuje „rzutu”, czyli losowego wyboru orzeł / reszka
# komputer wyświetla wynik rzutu
# jeżeli wygrał użytkownik, to dodaje punkt dla użytkownika, jeżeli komputer to dodaje punkt dla komputera
# wyświetla wyniki
# wracamy do pierwszego punktu programu(wykorzystaj pętle).


import random
import time

# inicjalizacja wyników
user_score = 0
computer_score = 0


def check_input(user_choice):
    if user_choice == 'o':
        return True
    elif user_choice == 'r':
        return False
    else:
        print("Niepoprawny wybór!")
        return None


def check_win(user_choice, user_score, computer_score):
    coin_toss = random.choice([True, False])
    if coin_toss:
        print("Wypadł orzeł!")
    else:
        print("Wypadła reszka!")

    if user_choice == coin_toss:
        print("Wygrałeś!")
        user_score += 1
    else:
        print("Przegrałeś.")
        computer_score += 1

    # wyświetlanie wyniku
    print(f"Wynik: Użytkownik {user_score} - {computer_score} Komputer")


def wait():
    print("Trzy...")
    time.sleep(1)
    print("Dwa...")
    time.sleep(1)
    print("Jeden...")
    time.sleep(1)


# pętla gry
while True:
    print("Witaj w grze w rzut monetą!")
    user_choice = input("Wybierz orła (o) lub reszkę (r): ")
    user_choice_orzel = check_input(user_choice)

    wait()

    check_win(user_choice_orzel, user_score, computer_score)

    response = input("Czy chcesz zagrać jeszcze raz? (t/n): ")
    if response == 't':
        continue
    elif response == 'n':
        break
