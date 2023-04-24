# Utwórz 10-elementową listę, którą należy wypełnić elementami losowymi z zakresu [-10,10]

import random

list = [random.randint(-10, 10) for i in range(10)]
print('Lista: ', list)
