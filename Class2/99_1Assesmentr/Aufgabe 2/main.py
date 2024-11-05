from staubsauger import Staubsuager
from waschmaschine import Waschmaschine


def main():
    geraeteliste = [Waschmaschine(), Staubsuager()]

    for geraet in geraeteliste:
        geraet.anschalten()
        geraet.verwenden()


if __name__ == '__main__':
    main()
