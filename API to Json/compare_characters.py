import requests
from validate_api_response import validate_api_response


def get_character_species(species_url):
    species_response = requests.get(species_url)
    if validate_api_response(species_response):
        data = species_response.json()
        species_name = data['name']
        return species_name


def get_character_data(url):
    response = requests.get(url)
    if validate_api_response(response):
        data = response.json()
        if len(data['species']) != 0:
            character_species = get_character_species(data['species'][0])
        else:
            character_species = "N/A"

    character_data = {'name': data["name"],
                      'height': data["height"],
                      'weight': data["mass"],
                      'species': character_species
                      }

    return character_data


def compare_characters(character_1, character_2):
    print(character_1, character_2)

    return output_data


if __name__ == "__main__":
    character_1 = get_character_data("https://swapi.dev/api/people/1/")
    character_2 = get_character_data("https://swapi.dev/api/people/2/")

    print(compare_characters(character_1, character_2))
