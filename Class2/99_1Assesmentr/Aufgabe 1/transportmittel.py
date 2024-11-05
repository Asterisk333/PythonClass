from abc import abstractmethod


class Transportmittel:

    @abstractmethod
    def vorbereiten(self):
        pass

    @abstractmethod
    def bewegen(self):
        pass
