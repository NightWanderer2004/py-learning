# Zaprezentować wykorzystanie bibliotek pickle i joblib do serializacji oraz deserializacji różnych obiektów Pythona, wykonać serializację, deserializację do ciągu znakowego oraz zapis i odczyt do plików bez kompresji i z kompresją
import joblib

class Test_class():
    def __init__(self, name, age):
        self.name = name
        self.age = age
            
    def print(self):
        print(self.name, self.age)


joblib.dump(Test_class, 'class.joblib')
deserialized_class = joblib.load('class.joblib')
print(deserialized_class)