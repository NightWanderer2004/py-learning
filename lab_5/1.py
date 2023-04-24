# Napisz funkcję, która dla zadanego argumentu (którym może być lista, krotka lub inna sekwencja)
# zwraca indeks i wartość najmniejszego elementu oraz indeks i wartość największego elementu.
# Następnie, używając składni list comprehension utwórz kilkunastoelementową listę wypełnioną
# losowymi liczbami całkowitymi i przetestuj na niej swoją funkcję.
# Uwaga. Python posiada wbudowane funkcje min, max itp. do znalezienia maksimum, minimum
# oraz indeksów

import random


def min_max(seq):
    min_index = 0
    max_index = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_index]:
            min_index = i
        if seq[i] > seq[max_index]:
            max_index = i
    return min_index, seq[min_index], max_index, seq[max_index]


my_list = [random.randint(0, 100) for i in range(14)]

print(f"Min: {min_max(my_list)[1]}, index: {min_max(my_list)[0]}")
print(f"Max: {min_max(my_list)[3]}, index: {min_max(my_list)[2]}")
