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

# pętla gry
while True:
    print("Witaj w grze w rzut monetą!")
    user_choice = input("Wybierz orła (o) lub reszkę (r): ")
    if user_choice == 'o':
        user_choice_orzel = True
    else:
        user_choice_orzel = False

    print("Trzy...")
    time.sleep(1)
    print("Dwa...")
    time.sleep(1)
    print("Jeden...")
    time.sleep(1)

    # symulacja rzutu
    coin_toss = random.choice([True, False])

    # wyświetlanie wyniku
    if coin_toss:
        print("Wypadł orzeł!")
    else:
        print("Wypadła reszka!")

    # sprawdzanie wyniku i aktualizacja punktów
    if user_choice_orzel == coin_toss:
        print("Wygrałeś!")
        user_score += 1
    else:
        print("Przegrałeś.")
        computer_score += 1

    # wyświetlanie wyniku
    print(f"Wynik: Użytkownik {user_score} - {computer_score} Komputer")

    # pytanie o kolejną rundę
    response = input("Czy chcesz zagrać jeszcze raz? (t/n): ")
    if response != 't':
        break
