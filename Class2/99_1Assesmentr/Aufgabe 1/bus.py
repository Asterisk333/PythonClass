from transportmittel import Transportmittel


class Bus(Transportmittel):
    def vorbereiten(self):
        print("Bus wird Beladen")

    def bewegen(self):
        print("Bus faehrt")
