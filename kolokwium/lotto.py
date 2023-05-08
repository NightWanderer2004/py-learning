import random


def lotto():
    lotto = []
    while len(lotto) < 6:
        number = random.randint(1, 49)
        if number not in lotto:
            lotto.append(number)
    return lotto


def prompt(arr):
    while len(arr) < 6:
        number = int(input("Podaj liczbe: "))
        if number not in arr and number > 0 and number < 50:
            arr.append(number)
        else:
            print(
                "Prosze Podawac w zakresie od 0 do 49 i zeby liczby sie nie powtarzali")
    return arr


def check(user_arr, lotto_arr):
    correct = 0
    for number in user_arr:
        if number in lotto_arr:
            correct += 1

    sort_numbers(user_arr, lotto_arr)
    print("Trafione liczby:", correct)


def sort_numbers(user_arr, lotto_arr):
    user_arr.sort()
    lotto_arr.sort()
    print("Twoje liczby:", user_arr)
    print("Wynik losowania:", lotto_arr)


def to_binary(lotto_arr):
    binary_numbers = []
    for number in lotto_arr:
        binary_numbers.append(bin(number))
    print(binary_numbers)


print("Witaj w symulatorze LOTTO!")

rand_lotto = lotto()
print("Lotto:", rand_lotto)

user_input = []
user_input = prompt(user_input)

check(user_input, rand_lotto)

to_binary(rand_lotto)
