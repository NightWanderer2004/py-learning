import numpy as np

def funkcja(x): # funkcja do której szukamy pierwiastka
    return (np.exp(5*x)/100) - 1/4 

def pochodna(x): # pochodna funkcji
    return 5*np.exp(5*x)/100

def metoda_newtona(x0, delta): # metoda Newtona
    iteracje = 0
    x = x0
    while abs(funkcja(x)) > delta: # warunek kończący iteracje, jeśli znaleziono pierwiastek z dostatecznie małą dokładnością
        x = x - funkcja(x) / pochodna(x) 
        iteracje += 1 
    pierwiastek = x
    return pierwiastek, iteracje # zwracamy znaleziony pierwiastek i liczbę iteracji

delta = 1e-5 # dokładność szukania pierwiastka
x0_1 = 0.05 # punkt startowy algorytmu
x0_2 = 0.9 # punkt startowy algorytmu

pierwiastek_1, iteracje_1 = metoda_newtona(x0_1, delta) # wywołujemy funkcję
print("Dla x0 = 0.05:") # wypisujemy wyniki
print("Pierwiastek: ", pierwiastek_1) # wypisujemy wyniki
print("Liczba iteracji: ", iteracje_1)

pierwiastek_2, iteracje_2 = metoda_newtona(x0_2, delta) # wywołujemy funkcję
print("Dla x0 = 0.9:") # wypisujemy wyniki
print("Pierwiastek: ", pierwiastek_2) 
print("Liczba iteracji: ", iteracje_2) 
