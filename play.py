import random
import json
from functools import reduce


def generate_number():
    return random.randint(1, 100)


def process_input(user_input):
    try:
        number = int(user_input)
        if 1 <= number <= 100:
            return number
        else:
            print("Bitte eine Zahl zwischen 1 und 100 eingeben.")
            return None
    except ValueError:
        print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
        return None


def compare_numbers(guessed_number, target_number):
    if guessed_number < target_number:
        return "zu niedrig"
    elif guessed_number > target_number:
        return "zu hoch"
    else:
        return "richtig"


def load_highscore():
    try:
        with open('highscore.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None


def save_highscore(name, points):
    highscore = load_highscore()
    if highscore is None or points > highscore['points']:
        with open('highscore.json', 'w') as file:
            json.dump({'name': name, 'points': points}, file)
        print(f"Neuer Highscore! {name} mit {points} Punkten.")


def game():
    target_number = generate_number()
    attempts = 0

    print("Willkommen zum Zahlenratespiel!")
    print("Ich habe eine Zahl zwischen 1 und 100 gewählt. Kannst du sie erraten?")

    difficulty = input("Wähle einen Schwierigkeitsgrad (einfach, mittel, schwer): ").lower()
    difficulty_dict = {'einfach': 15, 'mittel': 10, 'schwer': 5}
    max_attempts = difficulty_dict.get(difficulty, 5)

    attempt_list = []

    while attempts < max_attempts:
        user_input = input("Gib deine Zahl ein: ")
        guessed_number = process_input(user_input)
        if guessed_number is None:
            continue

        attempts += 1
        result = compare_numbers(guessed_number, target_number)
        if result == "richtig":
            points = max_attempts - attempts + 1
            print(
                f"Glückwunsch! Du hast die Zahl {target_number} in {attempts} Versuchen erraten und {points} Punkte "
                f"erzielt.")
            name = input("Gib deinen Namen für den Highscore ein: ")
            save_highscore(name, points)
            break
        else:
            print(f"Deine Zahl ist {result}. Versuche es erneut.")

        # Append the result to the list of attempts
        attempt_list.append(attempts)

    if attempts == max_attempts:
        print(f"Leider hast du die Zahl nicht erraten. Die richtige Zahl war {target_number}.")

    highscore = load_highscore()
    if highscore:
        print(f"Aktueller Highscore: {highscore['name']} mit {highscore['points']} Punkten.")

    # Use map to convert list of attempts to strings and print them
    print("Liste der Versuche: ", list(map(str, attempt_list)))

    # Use filter to get valid attempts (in this case, all are valid)
    valid_attempts = list(filter(lambda x: x <= max_attempts, attempt_list))
    print("Gültige Versuche: ", valid_attempts)

    # Use reduce to calculate the total number of attempts
    total_attempts = reduce(lambda x, y: x + y, valid_attempts, 0)
    print(f"Gesamtanzahl der Versuche: {total_attempts}")


game()
