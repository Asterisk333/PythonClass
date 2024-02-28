# Schreibe ein Python-Programm, um die größte Zahl aus einer Liste zu ermitteln

liste = [1,2,3,4,9,5,6,7]
high = liste[0]

for listentry in liste:
    if listentry > high:
        high = listentry

print(high)