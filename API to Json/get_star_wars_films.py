import requests
from validate_api_response import validate_api_response


def get_star_wars_films():
    url = "https://swapi.dev/api/films/"
    response = requests.get(url)
    if validate_api_response(response):
        data = response.json()
        films = sorted(data["results"], key=lambda x: x["episode_id"])

        for film in films:
            print(f"{film['episode_id']}. {film['title']}")


if __name__ == "__main__":
    get_star_wars_films()
