from pymongo import MongoClient
from pymongo.errors import OperationFailure

print("TEST ADMIN")

# Connexion avec l'utilisateur admin
admin_client = MongoClient(
    "mongodb://admin:AdminPassword123!@localhost:27017/?authSource=admin"
)

db = admin_client["healthcare_db"]
collection = db["patients"]

# CREATE admin
collection.insert_one({
    "Name": "Test User",
    "Age": 99,
    "Gender": "Male"
})
print("ADMIN CREATE OK")

# READ admin
patient = collection.find_one({"Name": "Test User"})
print("ADMIN READ OK :", patient)

# UPDATE admin
collection.update_one(
    {"Name": "Test User"},
    {"$set": {"Age": 100}}
)
print("ADMIN UPDATE OK")

# DELETE admin
collection.delete_one({"Name": "Test User"})
print("ADMIN DELETE OK")


print("\nTEST READER_USER")

# Connexion avec l'utilisateur reader
reader_client = MongoClient(
    "mongodb://reader_user:ReaderPassword123!@localhost:27017/healthcare_db?authSource=healthcare_db"
)

reader_db = reader_client["healthcare_db"]
reader_collection = reader_db["patients"]

# READ 
reader_collection.find_one()
print("READER READ OK")

# WRITE

try:
    reader_collection.insert_one({
        "Name": "Should Fail",
        "Age": 0
    })
    print("ERREUR : reader_user a pu écrire")
except OperationFailure:
    print("READER WRITE REFUSÉ OK")
