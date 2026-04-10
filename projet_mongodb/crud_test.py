from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["healthcare_db"]
collection = db["patients"]

print("Test CRUD")

# CREATE
new_patient = {
    "Name": "Test User",
    "Age": 99,
    "Gender": "Male"
}
collection.insert_one(new_patient)
print("CREATE OK")

# READ
patient = collection.find_one({"Name": "Test User"})
print("READ OK :", patient)

# UPDATE
collection.update_one(
    {"Name": "Test User"},
    {"$set": {"Age": 100}}
)
print("UPDATE OK")

# DELETE
collection.delete_one({"Name": "Test User"})
print("DELETE OK")