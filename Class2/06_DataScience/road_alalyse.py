import pandas as pd

df = pd.read_csv('road_accident_dataset.csv')

age_group_counts = df.groupby('Driver Age Group').size().sort_values(ascending=False)

print(age_group_counts)