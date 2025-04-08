# Region,Country,Item Type,Sales Channel,Order Priority,Order Date,Order ID,
# Ship Date,Units Sold,Unit Price,Unit Cost,Total Revenue,Total Cost,Total Profit

import pandas as pd

df = pd.read_csv('GrosseDatenmengen.csv')

#
regionen = [
    "Europe",
    "Asia",
    "Central America and the Caribbean"
]

kategorien = [
    "Beverages",
    "Snacks"
]

region = regionen[0]
kategorie = kategorien[0]


def berechne_werte(region, kategorie):
    gefiltert = df[(df["Region"] == region) & (df["Item Type"] == kategorie)]
    total_revenue = gefiltert["Total Revenue"].sum()
    total_cost = gefiltert["Total Cost"].sum()
    total_profit = gefiltert["Total Profit"].sum()
    return total_revenue, total_cost, total_profit


print("\nAuswerung der Daten:\n")
print(f"{'Region':<35}{'Kategorie':<15}{'Total Revenue':<15}{'Total Cost':<15}{'Total Profit':<15}")

for region in regionen:
    for kategorie in kategorien:
        revenue, cost, profit = berechne_werte(region, kategorie)
        print(f"{region:<35}{kategorie:<15}{revenue:<15,.2f}{cost:<15,.2f}{profit:<15,.2f}")
