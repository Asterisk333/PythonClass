from bus import Bus
from roller import Roller


def main():
    transportmittel_list = [Bus(), Roller()]

    for transportmittel in transportmittel_list:
        transportmittel.vorbereiten()
        transportmittel.bewegen()


if __name__ == '__main__':
    main()
