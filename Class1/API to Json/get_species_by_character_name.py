import requests
from validate_api_response import validate_api_response


def get_species_by_character_name():
    character_name = input("Name: ")
    search_url = f"https://swapi.dev/api/people/?search={character_name}"
    response = requests.get(search_url)
    if validate_api_response(response):
        data = response.json()
        character_name = data["results"][0]["name"]

        # data output to demonstrate try/except
        # print(data)

        try:
            species_url = data["results"][0]["species"][0]
            species_response = requests.get(species_url)
            if validate_api_response(species_response):
                species_data = species_response.json()
                species_name = species_data["name"]
        except IndexError:
            species_name = "None"

        print(f"Spezies von {character_name}: {species_name}")
    else:
        print(f"Kein Charakter mit dem Namen {character_name} gefunden.")


if __name__ == "__main__":
    get_species_by_character_name()
