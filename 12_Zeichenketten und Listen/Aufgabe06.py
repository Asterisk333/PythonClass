# Schreiben Sie eine Python-Funktion, die zwei Listen annimmt und True zurückgibt, wenn sie mindestens ein gemeinsames
# Element haben.

liste = [1, 2, 3, 4, 5, 6, 7, 8]
liste2 = [10, 20, 30, 40, 50, 6, 70]


def listchecker(liste, liste2):
    for checker in liste:
        for checked in liste2:
            if checker == checked:
                print(checker, checked)
                return True

    return False


print(listchecker(liste, liste2))
