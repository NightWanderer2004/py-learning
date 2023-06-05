import random


# Zadanie 1
def fib(n):
    if n <= 0:
        print("Wartość n musi być dodatnią liczbą całkowitą.")
        return
    else:
        sequence = []
        a, b = 0, 1

        for i in range(n):
            sequence.append(a)
            a, b = b, a + b

        return sequence


# Zadanie 2
def check_input(value):
    try:
        n = int(value)
        return n
    except ValueError:
        print("Podana wartość musi być liczbą całkowitą.")


# Zadanie 3
def calc_median(list):
    sorted_list = sorted(list)
    n = len(sorted_list)
    mid = n // 2

    if n % 2 == 0:
        a = sorted_list[mid - 1]
        b = sorted_list[mid]
        median = (a + b) / 2
    else:
        median = sorted_list[mid]

    return median


def count_elements(list):
    average = sum(list) / len(list)
    count_small = 0
    count_large = 0

    for num in list:
        if num < average:
            count_small += 1
        elif num > average:
            count_large += 1

    return count_small, count_large


def random_list(list):
    random.shuffle(list)
    return list


def sort_list(list):
    sorted_list = sorted(list)
    sorted_list.reverse()
    return sorted_list


n = input("Podaj liczbę n: ")
n = check_input(n)

fibonacci_list = fib(n)
print("Ciąg Fibonacci: ", fibonacci_list)

median = calc_median(fibonacci_list)
print("Mediana: ", median)

small, large = count_elements(fibonacci_list)
print("Liczba elementów mniejszych od średniej:", small)
print("Liczba elementów większych od średniej:", large)

rand_list = random_list(fibonacci_list)
print("Przemieszana lista: ", rand_list)

sorted_list = sort_list(fibonacci_list)
print("Posortowana lista malejąco: ", sorted_list)
