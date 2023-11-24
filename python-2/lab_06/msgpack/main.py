# Wykorzystać bibliotekę MessagePack do serializacji i deserializacji oraz porównać wielkość danych po serializacji z formatem JSON i YAML
import json
import yaml
import msgpack

data = {
    'title': 'Nier: Automata',
    'release': 2017,
    'developer': 'Platinum Games',
    'publisher': 'Square Enix',
    'platforms': ['PC', 'PS4', 'XONE'],
    'genre': 'Action RPG',
}

json_data = json.dumps(data)
json_size = len(json_data)

yaml_data = yaml.dump(data, default_flow_style=False)
yaml_size = len(yaml_data)

msgpack_data = msgpack.packb(data)
msgpack_size = len(msgpack_data)

print(f"JSON Size: {json_size} bytes")
print(f"YAML Size: {yaml_size} bytes")
print(f"MessagePack Size: {msgpack_size} bytes")
