# Zaprezentować wykorzystanie biblioteki JSON do serializacji oraz deserializacji różnych typów danych i zapisu oraz odczytu plików
import json

data = {
    'name' : 'Eduard',
    'age' : 19,
    'hobby' : 'japan games'
}

# Dumping data to json
json_data = json.dumps(data)
print(type(json_data))
print(json_data)


# Loading data from json
res_data = json.loads(json_data)
print(type(res_data))
print(res_data)