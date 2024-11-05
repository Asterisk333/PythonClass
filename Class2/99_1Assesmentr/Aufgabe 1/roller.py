from transportmittel import Transportmittel


class Roller(Transportmittel):
    def vorbereiten(self):
        print("der roller benoetigt keine Vorbereitung")

    def bewegen(self):
        print("der bewegt sich")
