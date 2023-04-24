# Utwórz słownik składający się z 10 elementów zawierający jako klucze nazwy produkt1, produkt2,
# itd.,natomiast jako wartości liczby zmiennoprzecinkowe będące ceną produktu. Napisz funkcję,
# która wypisze 3 najdroższe oraz 3 najtańsze produkty w postaci:
# produkt1 80.99
# produkt5 75.49
# ...
# Dodatkowo oblicz średnią cenę wszystkich produktów ze słownika.

products = {
    "product1": 80.99,
    "product2": 75.49,
    "product3": 50.99,
    "product4": 40.99,
    "product5": 30.99,
    "product6": 20.99,
    "product7": 10.99,
    "product8": 5.99,
    "product9": 4.99,
    "product10": 1.99
}


def three_expenstive(dict):
    sorted_dict = sorted(dict.items(), key=lambda x: x[1], reverse=True)
    new_dict = {sorted_dict[i] for i in range(3)}
    return new_dict


def three_cheapest(dict):
    sorted_dict = sorted(dict.items(), key=lambda x: x[1])
    new_dict = {sorted_dict[i] for i in range(3)}
    return new_dict


def average_price(dict):
    return sum(dict.values()) / len(dict)


print("Expenstive: ", three_expenstive(products))
print("Cheapest: ", three_cheapest(products))
print(f"Average price: {average_price(products):.2f}")
