import requests
from validate_api_response import validate_api_response


def get_luke_skywalker_data():
    url = "https://swapi.dev/api/people/1/"
    response = requests.get(url)
    if validate_api_response(response):
        data = response.json()

        name = data["name"]
        height = data["height"]
        birth_year = data["birth_year"]

        print(f"Name: {data["name"]}")
        print(f"Grösse: {data["height"]} cm")
        print(f"Geburtsjahr: {data["birth_year"]}")


if __name__ == "__main__":
    get_luke_skywalker_data()
