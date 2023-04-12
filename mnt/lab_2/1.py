# Zadanie 1
# Uruchom i przeanalizuj poniższy kod programu. Wskaż, którą z powyższych metod
# wykorzystano? Opisz krótko działanie zamieszczonego programu.

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + x - 1

# Создаем массив значений аргумента функции от -1 до 1 с шагом 0.01
t = np.arange(-1, 1, 0.01)

# Строим график функции
plt.plot(t, f(t))
plt.grid(True)
plt.xlabel('$x$')
plt.ylabel('$y(x)$')

# Задаем начальные значения для поиска корня
a = t[0]
b = t[-1]
e = 1e-4
iMax = 100

# Используем метод бисекции для нахождения корня уравнения
for k in range(iMax):
    x = (a + b) / 2
    if abs(f(x)) < e:
        yo = f(x)
        xo = x
        break
    elif f(a) * f(x) < 0:
        b = x
    else:
        a = x

# Отображаем найденный корень на графике
plt.plot(xo, yo, 'ro')

# Отображаем график функции и найденного корня
plt.show()
