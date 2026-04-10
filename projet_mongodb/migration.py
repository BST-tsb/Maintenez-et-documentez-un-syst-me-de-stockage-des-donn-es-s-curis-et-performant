import pandas as pd
from pymongo import MongoClient

print("Début migration")

# Connexion MongoDB
client = MongoClient("mongodb://mongo:27017/")
db = client["healthcare_db"]
collection = db["patients"]

# Charger CSV
df = pd.read_csv("healthcare_dataset.csv")

print("CSV chargé")

# Nettoyage
df = df.drop_duplicates()

# Conversion dates
df["Date of Admission"] = pd.to_datetime(df["Date of Admission"])
df["Discharge Date"] = pd.to_datetime(df["Discharge Date"])

# Conversion en dictionnaire
data = df.to_dict(orient="records")

# Insertion
collection.insert_many(data)

print("Données insérées dans MongoDB")