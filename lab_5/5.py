# Wczytaj od użytkownika wartość klucza, następnie wypisz wartość przypisaną mu w słowniku.
# W przypadku, gdy klucz nie istnieje powiadom o tym użytkownika.

my_dict = {"a": 1, "b": 2, "c": 3}
print(my_dict)
user_choice = input("Enter key: ")

print(my_dict.get(user_choice, "Key not found"))
