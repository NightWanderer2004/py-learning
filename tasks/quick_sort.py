list = [4, 5, 13, 52, 1, 6]


def quick_sort(list):
    if len(list) < 2:
        return list
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print("Quick sort:")
print(list)
print(quick_sort(list))


def find_kth_smallest(list, k):
    if len(list) < 2:
        return list[0]
    else:
        pivot = list[0]
        less = [i for i in list[1:] if i <= pivot]
        greater = [i for i in list[1:] if i > pivot]
        if len(less) == k - 1:
            return pivot
        elif len(less) > k - 1:
            return find_kth_smallest(less, k)
        else:
            return find_kth_smallest(greater, k - len(less) - 1)


print("Find kth smallest:")
print(list)
print(find_kth_smallest(list, 2))
