# Napisz funkcję, która:
# a) doda nowy element do istniejącego słownika;
# b) połączy zawartość trzech słowników w jeden;
# c) sprawdzi czy dany klucz występuje już w słowniku;
# d) wygeneruje i wypisze na ekran słownik o kluczach wartości 1-n, gdzie n poda użytkownik;
# dla każdego klucza x, wartość elementu ma wynosić x do potęgi drugiej;
# e) znajdzie największą wartość całkowitą w słowniku;
# f) zsumuje wszystkie wartości ze słownika

def add_to_dict(dict, key, value):
    dict[key] = value
    return dict


my_dict = {"a": 1, "b": 2, "c": 3}
print("a) Before", my_dict)
add_to_dict(my_dict, "d", 4)
print("a) After", my_dict)


def merge_dicts(dict1, dict2, dict3):
    return {**dict1, **dict2, **dict3}


dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}
print("b) Dict1: ", dict1, "Dict2: ", dict2, "Dict3: ", dict3)
newDict = merge_dicts(dict1, dict2, dict3)
print("b) newDict:", newDict)


def check_key(dict, key):
    return key in dict


print("c) Key 'a' in dict:", check_key(my_dict, "a"))
print("c) Key 'y' in dict:", check_key(my_dict, "y"))


def generate_dict(n):
    return {x: x ** 2 for x in range(1, n + 1)}


print("d) Dict:", generate_dict(5))


def find_max(dict):
    return max(dict.values())


print("e) Max value:", find_max(my_dict))


def sum_dict(dict):
    return sum(dict.values())


print("f) Sum of values:", sum_dict(my_dict))
