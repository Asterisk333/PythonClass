import random

print("Willkommen zu Schere Stein Papier!")

gesten = ["Schere", "Stein", "Papier"]
computer_geste = random.choice(gesten)

spieler_geste = None
while spieler_geste not in gesten:
    print("Verfügbare Gesten: ", *gesten)
    spieler_geste = input("Bitte wählen Sie eine Geste aus: ")

print(f"Sie haben {spieler_geste} gewählt, der Computer {computer_geste}: ", end="")
if spieler_geste == computer_geste:
    print("Unentschieden!")
elif spieler_geste == "Schere" and computer_geste == "Papier" or \
        spieler_geste == "Stein" and computer_geste == "Schere" or \
        spieler_geste == "Papier" and computer_geste == "Stein":
    print("Sie haben gewonnen!")
else:
    print("Leider verloren")
