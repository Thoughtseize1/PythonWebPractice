from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Thoughtseize_:JYX9gGFssSqILal9@nickitm.rj1lqrb.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command("ping")
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

database = client.web9_thoughtseize
collection_with_cats = database.FirstColl

if __name__ == "__main__":
    # Creates a collection if there is no collection.
    collection_with_owners = database.Owners
    # Inserts a new user (if not already)
    collection_with_owners.insert_one(
        {
            "name": "Nikita",
            "age": 28,
            "breed": "Human",
            "color": "white",
            "weight": 82,
        }
    )
    # Places the cursor on all documents in the collection in the results
    results = collection_with_cats.find()
    for its in results:
        print(its)
