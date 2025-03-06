import pandas as pd
import json
import numpy as np

with open("produkte.json", "r", encoding="utf-8") as file:
    data = json.load(file)

df = pd.json_normalize(data, sep="_")

print(df.columns)

## Sum sum with for each I think

df.fillna()


df.to_csv("produkte.csv", index=False)

print(df)
