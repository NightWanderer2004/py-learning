# Zaprezentować wykorzystanie biblioteki YAML do serializacji oraz deserializacji różnych typów danych i zapisu oraz odczytu plików
import yaml
import os 

dir = os.path.dirname(__file__)

# Read
with open(f'{dir}/data.yaml', 'r') as file:
    data = yaml.safe_load(file)

print(data)


# Write
new_data = {
    "title": "Nier:Automata",
    "developer": "PlatinumGames",
    "genre": "Action RPG, drama",
    "platform": "PlayStation 4, Xbox One, Microsoft Windows",
    "release_date": "2017-02-23",
    "publisher": "Square Enix",
}

with open(f'{dir}/data.yaml', encoding='utf-8', mode='w') as file:
    data['games'].append(new_data)
    yaml.dump(data, file, default_flow_style=False, allow_unicode=True) # allow_unicode=True - for saving japanese characters
