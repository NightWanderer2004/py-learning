# Napisz funkcję, która dla dowolnej sekwencji podanej jako argument, obliczy ile razy wystąpił w
# niej każdy z elementów i zwróci te dane jako wynik. Następnie wypisz liczbę wystąpień każdego
# elementu na ekran zaczynając od elementu najmniejszego. Niezbędne sortowanie powinno się odbyć już poza funkcją.
# Wersja podstawowa: w funkcji utwórz słownik, w którym kluczami są poszczególne elementy sekwencji, a wartościami - liczba ich wystąpień.
# Wersja rozszerzona: Możesz stworzyć drugą funkcję, która użyje Countera
# (https://docs.python.org/3/library/collections.html#collections.Counter). Counter obsługuje
# składnię słownika, dlatego samo wypisywanie na ekran powinno działać dokładnie tak samo jak
# dla funkcji z wersji podstawowej.

# Do sortowania można użyć wbudowanej funkcji sorted.
# Np. dla napisu "abzkfhiohfnlaanfnffnkkdamd" na ekran powinno się wypisać:
# a: 4
# b: 1
# d: 2
# f: 5
# h: 2
# i: 1
# k: 3
# l: 1
# m: 1
# n: 4
# o: 1
# z: 1

from collections import Counter


def count_symbols(seq):
    dict = {}
    for i in seq:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return sorted(dict.items())


def with_counter(seq):
    counted = Counter(seq)
    return sorted(counted.items())


# counted = count_symbols("abzkfhiohfnlaanfnffnkkdamd")
counted = with_counter("abzkfhiohfnlaanfnffnkkdamd")
print(counted)
