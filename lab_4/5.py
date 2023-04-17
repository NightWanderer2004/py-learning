# Napisz program, który utworzy i wypisze listę składającą się z n losowych liczb całkowitych z przedziału [1,50],
# a następnie po każdej liczbie podzielnej przez 3 wstawi nowy element o wartości 0; na koniec wyświetli tak zmodyfikowaną listę

import random

list = [random.randint(1, 50) for i in range(4)]
print("Before:", list)
mod_list = []
for i in list:
    mod_list.append(i)
    if i % 3 == 0:
        mod_list.append(0)

print("After: ", mod_list)
