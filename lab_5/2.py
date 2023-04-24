# Dana jest tablica o wymiarach n × n. Napisz funkcję, która wypisze zawartość jedynie tych wierszy
# tablicy, w których wszystkie elementy są większe od liczby 2

def print_rows(arr):
    for row in arr:
        if all([x > 2 for x in row]):
            print(row)


table = [[13, 3, 4], [4, 4, 4], [0, 2, -2]]

print_rows(table)
