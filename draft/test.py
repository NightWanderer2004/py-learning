# print("Cytat z Ojca Chrzestnego: \n",
#       "It's not personal. It's strictly business.")

# print("Cytat z Ojca Chrzestnego: \nIt's not personal. It's strictly business.\n" * 5)

# print("**********")
# print("*        *")
# print("*        * b")
# print("*        * ")
# print("**********")
# print("    ", "a", "  ")


# def farenheit(far):
#     far = far + 32
#     return far


# cel = float(input("Podaj liczbę w celsjuszach: "))

# print("Temperatura w Fahrenheicie to: ", farenheit(cel))

# Napisz program proszący użytkownika o podanie dwóch liczb a, b i wypisujący ich sumę, różnicę,
# iloczyn, iloraz, √𝑎 + 𝑏 oraz 𝑎𝑏.


# (FizzBuzz) Napisz program, w którym użytkownik podaje kilka razy liczby całkowitą. Jeśli
# użytkownik poda liczbę podzielną przez 3, to wypisz na ekranie słowo „Fizz”, natomiast
# gdy poda liczbę podzielną przez 5, wypisz słowo „Buzz”. W przypadku liczb podzielnych zarówno
# przez 3 i 5, wypisz słowo „FizzBuzz”.


# # przeczytaj trzy liczby
# liczba_1 = int(input("Wprowadz pierwsza liczbe: "))
# liczba_2 = int(input("Wprowadz druga liczbe: "))
# liczba_3 = int(input("Wprowadz trzecia liczbe: "))

# # sprawdz, ktora z liczb jest najwieksza
# # i przekaz ja do zmiennej najwieksza_liczba

# najwieksza_liczba = max(liczba_1, liczba_2, liczba_3)

# # wyswietl wynik
# print("Najwieksza liczba jest:", najwieksza_liczba)


# value = input("Podaj nazwę rośliny: ")

# if value.lower() == "skrzydłokwiat".lower():
# 	print("Skrzydłokwiat jest najlepszą rośliną w historii!")
# else:
# 	print("Nie, ja chcę Skrzydłokwiat...!")

#Instrukcja break służy do wyjścia z/przerwania pętli.



# Zaprojektuj program wykorzystujący pętlę while, który ciągle prosi użytkownika o wpisanie słowa, chyba że użytkownik wprowadzi słowo "pumpernikiel" - w takim przypadku wyświetl na konsoli wiadomość "Udało ci się opuścić pętlę." i przerwij tę pętlę.

# while True:
# 	value = input("Podaj słowo: ")
# 	if value.lower() == "pumpernikiel":
# 		print("Udało ci się opuścić pętlę.")
# 		break
# 	else:
# 		print("Nie, ja chcę pumpernikiel...!")


# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch, end="")

# for cyfra in "0165031806510":
#     if cyfra == "0":
#         print("x", end="")
#         continue
#     print(cyfra, end="")



