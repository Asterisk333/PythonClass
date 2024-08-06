# Aufgabe 5: Entwickeln Sie ein Python-Programm, das eine Zahl n akzeptiert und ein Muster wie folgt ausgibt:
# Für n = 3 sollte das Muster sein:
# 1
# 2 2
# 3 3 3
# Für n = 5 sollte das Muster sein:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

def muster(n):
    for i in range(1, n + 1):
        print((str(i) + ' ') * i)


muster(3)
muster(5)
muster(10)
