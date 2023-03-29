# Zapoznać się z podstawami języka Python. Uruchomić i zmodyfikować przykłady z instrukcji

spam = [10, 21, 23, 11, 24]  # definujemy listę

spam.append(11)  # dodajemy element do listy o wartości 11
print("lista: ", spam)  # [10, 21, 23, 11, 24, 11]

# zliczamy wystąpienia elementu o wartości 11, wynik 2
print("ilość '11' w liscie: ", spam.count(11))
# zwraca indeks pierwszego wystąpienia elementu o wartości 11, wynik 3
print("index elementu o wartości '11'", spam.index(11))

spam.remove(11)  # usuwamy pierwsze wystąpienie elementu o wartości 11
print(spam)  # [10, 21, 23, 24, 11]

spam.sort()  # sortujemy listę (sortowanie rosnące)
print(spam)  # [10, 11, 21, 23, 24]

spam.reverse()  # odwracamy kolejność elementów w liście
print(spam)  # [24, 23, 21, 11, 10]
