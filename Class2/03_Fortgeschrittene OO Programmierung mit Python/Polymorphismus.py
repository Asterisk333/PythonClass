# Aufgabe1: Polymorphismus Erstellen Sie eine Klasse Tier mit einer Methode machen_sound. Erstellen Sie dann zwei
# Unterklassen Hund und Katze, die die Tier-Klasse erben. Überschreiben Sie die machen_sound-Methode für jede der
# Unterklassen, um einen Sound zu machen, der typisch für das Tier ist. Schreiben Sie schließlich eine Funktion
# mach_tier_sound, die ein Objekt der Klasse Tier als Argument nimmt und die machen_sound-Methode des Objekts aufruft.

class Tier:
    def machen_sound(self):
        pass


class Hund(Tier):
    def machen_sound(self):
        return "Wuff"


class Katze(Tier):
    def machen_sound(self):
        return "Miau"


def mach_tier_sound(tier_obj):
    return tier_obj.machen_sound()


# Beispielverwendung
hund = Hund()
katze = Katze()

print(mach_tier_sound(hund))  # Ausgabe: Wuff
print(mach_tier_sound(katze))  # Ausgabe: Miau
