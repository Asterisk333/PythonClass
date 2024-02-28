# ufgabe 2 [10 Punkte]:
# Schreiben Sie eine Funktion, die eine Liste von Wörtern erhält und eine Liste von Wörtern zurückgibt,
# die mit einem bestimmten Buchstaben beginnen, den der Benutzer angibt. Diesen Buchstaben dürfen Sie als
# fixe Variable definieren.

Userinput = "d"
liste = ["Dito", "Glumanda", "Bisasam", "Dragoran"]
neueliste = []

for wort in liste:
    if wort.lower().startswith(Userinput.lower()):
        neueliste.append(wort)

print(neueliste)
