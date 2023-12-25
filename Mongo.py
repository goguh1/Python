# Mondo Database DB Tutorial (local machine)​
​# Do:​

# Get started​
# Create database​
# Create Collections​
# Insert​

import pymongo

# Connect to the MongoDB server (default host and port)
client = pymongo.MongoClient("mongodb://localhost:27017/")

# Create or access a database (in this case, 'mydatabase')
db = client["mydatabase"]

# Create or access a collection (in this case, 'mycollection')
collection = db["mycollection"]

# Insert data into four different documents
for i in range(4):
    name = input(f"Enter name for document {i + 1}: ")
    location = input(f"Enter location {i + 1}: ")
    age = int(input(f"Enter age for document {i + 1}: "))

data = {
"name": name,
"location": location,
"age": age
}

inserted_document = collection.insert_one(data)
print(f"Inserted document {i + 1}, ID: {inserted_document.inserted_id}")

# Retrieve and print all documents in the collection
print("All documents in the collection:")
for document in collection.find():
    print(document)

# Close the MongoDB connection (not always necessary)
client.close()
