import pandas as pd

print("Script lancé")

df = pd.read_csv("healthcare_dataset.csv")

print("CSV chargé")

print(df.head())
print(df.info())
print(df.isnull().sum())