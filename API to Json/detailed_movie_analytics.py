import requests
from validate_api_response import validate_api_response


def get_character_species(species_url):
    species_response = requests.get(species_url)
    if validate_api_response(species_response):
        data = species_response.json()
        species_name = data['name']
        return species_name


def get_character_name(character_url):
    character_response = requests.get(character_url)
    if validate_api_response(character_response):
        data = character_response.json()
        character_name = data['name']
        if len(data['species']) != 0:
            character_species = get_character_species(data['species'][0])
        else:
            character_species = "N/A"

        print(f"{character_name}: {character_species}")


def get_star_wars_films():
    url = "https://swapi.dev/api/films/"
    response = requests.get(url)
    if validate_api_response(response):
        data = response.json()
        films = sorted(data["results"], key=lambda x: x["episode_id"])
        for film in films:
            print(f"{film['episode_id']}. {film['title']}")
            print("---------------------------------")
            for character in film["characters"]:
                get_character_name(character)


if __name__ == "__main__":
    get_star_wars_films()
