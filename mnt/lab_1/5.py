# Utworzyć skrypt który:
# 1. tworzy wektor wierszowy v0 o 10 elementach którego liczba początkowa to 0 a końcowa to 5
# 2. tworzy wektor v1 powstały przez dodanie liczby 5 do wektora v0
# 3. tworzy macierz A(2x10) przez konkatenacje wektorów v0 oraz v1

# 1.
from numpy import *  # importujemy moduł NumPy

v0 = r_[0:5:0.5]  # tworzymy wektor wierszowy v0 o 10 elementach
print("v0: ", v0)  # [0.  0.5 1.  1.5 2.  2.5 3.  3.5 4.  4.5]

# 2.
v1 = v0 + 5  # do wektora v0 dodajemy 5
print("v1: ", v1)  # [5.  5.5 6.  6.5 7.  7.5 8.  8.5 9.  9.5]

# 3.
A = c_[v0, v1]  # tworzymy macierz 2x10 za pomocą funkcji c_ (konkatenacja)
print("A: ", A)  # wynik:
'''
[[0.  5. ]
 [0.5 5.5]
 [1.  6. ]
 [1.5 6.5]
 [2.  7. ]
 [2.5 7.5]
 [3.  8. ]
 [3.5 8.5]
 [4.  9. ]
 [4.5 9.5]]
'''
