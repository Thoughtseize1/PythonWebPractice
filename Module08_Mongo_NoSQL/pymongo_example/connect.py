from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import configparser


config = configparser.ConfigParser()
config.read("mongoengine\config.ini")

mongo_user = config.get("DB", "user")
mongodb_pass = config.get("DB", "pass")
db_name = config.get("DB", "db_name")
domain = config.get("DB", "domain")

# connect to cluster on AtlasDB with connection string

uri = f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority"""

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
# Creates a collection if there is no collection.

collection_with_owners = database.Owners


def insert_owner(_name):
    collection_with_owners.insert_one(
        {
            "name": _name,
            "age": 28,
            "breed": "Human",
            "color": "white",
            "weight": 82,
        }
    )


def select():
    # Limit for 3 results only
    # shows without _id and breed
    selected_cats = collection_with_cats.find(
        {"age": {"$lte": 2}}, {"_id": 0, "breed": 0}
    ).limit(3)
    for cat in selected_cats:
        print(cat)


def show_all_cats():
    # Places the cursor on all documents in the collection in the results
    results = collection_with_cats.find()
    for its in results:
        print(its)


def delete_users_with_name(collection, name):
    count = collection.count_documents({"name": name})
    if count == 0:
        print(f"No documents found with name '{name}'")
        return
    elif count == 1:
        print(f"1 document found with name '{name}'. Deleting...")
        result = collection.delete_one({"name": name})
    else:
        print(f"{count} documents found with name '{name}'. Deleting...")
        result = collection.delete_many({"name": name})
    if result.deleted_count > 0:
        print(f"Deleted {result.deleted_count} documents with name '{name}'")
    else:
        print(f"No documents deleted with name '{name}'")


if __name__ == "__main__":
    for i in range(10):
        insert_owner("Katya")
    delete_users_with_name(collection_with_owners, "Katya")
