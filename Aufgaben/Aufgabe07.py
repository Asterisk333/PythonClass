preis = 5.9
name = input("Ihr Name lautet: ")
porzionen = 1

if name.lower() != "jerry":
    porzionen = int(input("Anzahl Porzionen"))

kosten = porzionen * preis

print('das essen Kostet', str(kosten))
