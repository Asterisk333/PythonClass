import numpy as np

temperaturen = {"Montag": 18, "Dienstag": 20, "Mittwoch": 22, "Donnerstag": 19, "Freitag": 21}
temp_array = np.array(list(temperaturen.values()))

print(f"Durchschnittstemperatur: {np.mean(temp_array)}")
print(f"Maximale Temperatur: {np.max(temp_array)}")
print(f"Minimale Temperatur: {np.min(temp_array)}")
