# Zaprezentować wykorzystanie bibliotek pickle i joblib do serializacji oraz deserializacji różnych obiektów Pythona, wykonać serializację, deserializację do ciągu znakowego oraz zapis i odczyt do plików bez kompresji i z kompresją
import pickle

serialized1 = pickle.dumps(['a', 'b', 'c'])
deserialized1 = pickle.loads(serialized1)
print(serialized1)
print(deserialized1)

print('---')

serialized2 = pickle.dumps({'a': 1, 'b': 2, 'c': 3})
deserialized2 = pickle.loads(serialized2)
print(serialized2)
print(deserialized2)
