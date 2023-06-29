# Найти K-й наименьший элемент в неотсортированном массиве. Дан массив целых чисел и число K. Необходимо найти K-й наименьший элемент в массиве.

# Напишите функцию find_kth_smallest(arr, k), которая принимает неотсортированный массив arr и число K, и возвращает K-й наименьший элемент в массиве.

# Возможный подход к решению:

# Используйте мин-кучу (min-heap) для хранения K наименьших элементов.
# Переберите все элементы массива и добавьте их в мин-кучу.
# Если размер мин-кучи превышает K, удалите минимальный элемент из кучи.
# В конце процесса, верхний элемент в мин-куче будет K-м наименьшим элементом.

import heapq

list = [7, 10, 4, 3, 20, 15]


def find_kth_smallest(arr, k):
    min_heap = []
    for i in arr:
        heapq.heappush(min_heap, -i)
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return -min_heap[0]


print("List: ", list)
print("5-th smallest element: ", find_kth_smallest(list, 5))
print("3-rd smallest element: ", find_kth_smallest(list, 3))
