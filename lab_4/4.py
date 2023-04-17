# Napisz program, który wypisze listę składającą się z n losowych liczb całkowitych z przedziału [1, 100], a następnie usunie z listy elementy z przedziału[25-40] oraz wyświetli tak zmodyfikowaną listę

import random

list = [random.randint(1, 100) for i in range(8)]
print("Before: ", list)
list = [i for i in list if i < 25 or i > 40]
print("After:", list)
