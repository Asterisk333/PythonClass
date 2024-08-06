import requests
from validate_api_response import validate_api_response


def get_species_by_character_name(vehicle_name=[], starship_name=[]):
    character_name = input("Name: ")
    search_url = f"https://swapi.dev/api/people/?search={character_name}"
    response = requests.get(search_url)
    if validate_api_response(response):
        data = response.json()
        character_name = data["results"][0]["name"]
        character_height = data["results"][0]["height"]
        character_birth_year = data["results"][0]["birth_year"]

        # data output to demonstrate try/except
        # print(data)

        homeworld_url = data["results"][0]["homeworld"]
        homeworld_response = requests.get(homeworld_url)
        if validate_api_response(homeworld_response):
            homeworld_data = homeworld_response.json()
            homeworld_name = homeworld_data["name"]

        vehicle_url = data["results"][0]["vehicles"]
        for vehicle in vehicle_url:
            vehicle_response = requests.get(vehicle)
            if validate_api_response(vehicle_response):
                vehicle_data = vehicle_response.json()
                vehicle_name.append(vehicle_data["name"])

        starship_url = data["results"][0]["starships"]
        for starship in starship_url:
            starship_response = requests.get(starship)
            if validate_api_response(starship_response):
                starship_data = starship_response.json()
                starship_name.append(starship_data["name"])

        print(f"Analyse von {character_name}, {character_height}, {character_birth_year}, {homeworld_name},"
              f" {vehicle_name}, {starship_name}")
    else:
        print(f"Kein Charakter mit dem Namen {character_name} gefunden.")


if __name__ == "__main__":
    get_species_by_character_name()
