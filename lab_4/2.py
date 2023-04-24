# Napisz program, który:
# a) zmodyfikuje listę podnosząc jej wszystkie elementy do sześcianu;
# b) obliczy iloczyn elementów listy;
# c) obliczy średnią arytmetyczną elementów listy;
# d) zliczy elementy nieparzyste oraz obliczy ich sumę;
# e) sprawdzi, czy wskazany element występuje w liście;
# f) dla danego elementu poda liczbę jego wystąpień w liście;
# g) znajdzie element maksymalny listy;
# h) znajdzie parę sąsiednich elementów o największej sumie;
# i) znajdzie drugi największy element listy

# a)
list = [1, 2, 3, 4, 5, 4]
list = [i**3 for i in list]
print("a) ", list)

# b)
print("b) ", sum(list))

# c)
avg = sum(list)/len(list)
print("c) ", avg)

# d)
odd = [i for i in list if i % 2 == 1]
print("d) ", odd)

# e)
elem = 64
print("e) ", elem in list)

# f)
sum_of_elems = list.count(elem)
print("f) ", sum_of_elems)

# g)
max_elem = max(list)
print("g) ", max_elem)

# h)
elem_left = list[list.index(max_elem) - 1]
elem_right = list[list.index(max_elem) + 1]
print("h) ", "left: ", elem_left, "right: ", elem_right)

# i)
second_max_elem = sorted(list)[-2]
print("i) ", second_max_elem)
