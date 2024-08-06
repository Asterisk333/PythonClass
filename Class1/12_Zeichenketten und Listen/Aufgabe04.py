# Schreiben Sie ein Python-Programm, um die Anzahl der ähnlichen Zeichenketten in einer gegebenen Liste 'Liste'
# von Zeichenketten zu zählen. Zwei Zeichenketten sind ähnlich, wenn:
# Die Länge der Zeichenketten ist >= 2 und das erste und letzte Zeichen sind gleich.

liste = ["es", "lari", "suessie", "leri", "shiro", "saal", "sozio"]
samestrinliste = []

for element in liste:
    if len(element) > 2:
        checker = element
        for checked in liste:
            if not checker == checked and checked[0] == checker[0] and checked[-1] == checker[-1]:
                samestrinliste.append(checked)

print(samestrinliste)
