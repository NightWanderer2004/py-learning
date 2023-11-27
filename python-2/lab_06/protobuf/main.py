# Wykorzystać bibliotekę Protocol Buffers do serializacji i przesyłania danych różnego typu przez sieć
from person_pb2 import Person

person = Person()
person.name = "John Doe"
person.id = 123
person.email = "john@example.com"

serialized_person = person.SerializeToString()

new_person = Person()
new_person.ParseFromString(serialized_person)

print(f"Name: {new_person.name}")
print(f"ID: {new_person.id}")
print(f"Email: {new_person.email}")


