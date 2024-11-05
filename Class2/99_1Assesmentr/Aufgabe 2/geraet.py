from abc import abstractmethod


class Haushaltsgeraet:

    @abstractmethod
    def anschalten(self):
        pass

    @abstractmethod
    def verwenden(self):
        pass
