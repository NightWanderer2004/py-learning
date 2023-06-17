list = [3, 14, 1, 8, 4, 32, 5]


def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list


print("Bubble sort:")
print(list)
print(bubble_sort(list))


def reverse_bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] < list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list


print("Reverse bubble sort:")
print(list)
print(reverse_bubble_sort(list))
