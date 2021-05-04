import json
from pathlib import Path

def find_pokemon(name, json_file):
    arquivo_json = Path(json_file).read_text()
    pokemon_json = json.loads(arquivo_json)

    for index, pokemon in enumerate(pokemon_json):
        if pokemon_json[index]['name'] == name:
            for key, value in pokemon.items():
                print(key, value)
            return "This pokemon exist in database."
    return "This pokemon doesn't exist in database."

print(find_pokemon('Ditto' ,'curso\\pokemon.json'))