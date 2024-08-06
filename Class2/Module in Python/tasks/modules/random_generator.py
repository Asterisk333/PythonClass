import random
import string


def generate_random_number():
    return random.randint(1, 100)


def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))


