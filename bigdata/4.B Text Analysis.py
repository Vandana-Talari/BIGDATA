import pymongo

# Connection setup
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mybigdata"]
mycol = mydb["student"]

# Data list
mylist = [
    {"name": "Khyati", "address": "Mumbai"},
    {"name": "Kruti", "address": "Mumbai"},
    {"name": "Nidhi", "address": "Pune"},
    {"name": "Komal", "address": "Pune"}
]

# Data insert karna
x = mycol.insert_many(mylist)

# Check karne ke liye IDs print karein
print("Data successfully inserted in MongoDB!")
print("Inserted IDs:", x.inserted_ids)
