# Utwórz dwa zbiory i wypełnij je kilkoma losowymi liczbami całkowitymi z dowolnego przedziału,
# np. od 1 do 10 (przedział nie powinien być zbyt szeroki, żeby zbiory mogły mieć jakąś część wspólną).
# Następnie wypisz ich: sumę, różnicę i część wspólną, a także te elementy, które pojawiają się tylko w jednym z nich.

import random

list1 = [random.randint(1, 10) for i in range(10)]
list2 = [random.randint(1, 10) for i in range(10)]


def sum(list1, list2):
    return list1 + list2


def difference(list1, list2):
    return list(set(list1) - set(list2))


def intersection(list1, list2):
    return list(set(list1) & set(list2))


def only_in_one(list1, list2):
    return list(set(list1) ^ set(list2))


print(f"Sum: {sum(list1, list2)}")
print(f"Difference: {difference(list1, list2)}")
print(f"Intersection: {intersection(list1, list2)}")
print(f"Only in one: {only_in_one(list1, list2)}")
