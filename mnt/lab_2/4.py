import numpy as np

def funkcja(x):
    return (np.exp(5*x)/100) - 1/4

def pochodna(x):
    return 5*np.exp(5*x)/100

def metoda_newtona(x0, delta):
    iteracje = 0
    x = x0
    while abs(funkcja(x)) > delta:
        x = x - funkcja(x) / pochodna(x)
        iteracje += 1
    pierwiastek = x
    return pierwiastek, iteracje

delta = 1e-5
x0_1 = 0.05
x0_2 = 0.9

pierwiastek_1, iteracje_1 = metoda_newtona(x0_1, delta)
print("Dla x0 = 0.05:")
print("Pierwiastek: ", pierwiastek_1)
print("Liczba iteracji: ", iteracje_1)

pierwiastek_2, iteracje_2 = metoda_newtona(x0_2, delta)
print("Dla x0 = 0.9:")
print("Pierwiastek: ", pierwiastek_2)
print("Liczba iteracji: ", iteracje_2)
