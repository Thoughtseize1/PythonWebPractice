import argparse
from pprint import pprint
from bson.objectid import ObjectId
import configparser

from pymongo import MongoClient
from pymongo.server_api import ServerApi

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

# Creating database CATS
db = client.cats
poland_cats = db.cats_pl

parser = argparse.ArgumentParser(description="Cats APP")
parser.add_argument("--action", help="Command: create, update, find, remove")
parser.add_argument("--id")
parser.add_argument("--name")
parser.add_argument("--newname")
parser.add_argument("--age")
parser.add_argument("--update_name")
parser.add_argument("--features", nargs="+")

arguments = parser.parse_args()
my_arg = vars(arguments)

action = my_arg.get("action")
name = my_arg.get("name")
new_name = my_arg.get("newname")
age = my_arg.get("age")
_id = my_arg.get("id")
features = my_arg.get("features")


class ExceptValidation(Exception):
    pass


def find_cats():
    return poland_cats.find()


def find_cat(_id):
    return poland_cats.find_one({"_id": ObjectId(_id)})


def create_cat(name_: str, age_: str, features_: list):
    result = poland_cats.insert_one(
        {"name": name_, "age": int(age_), "features": features_}
    )
    # The insert_one() method returns a InsertOneResult object, which has a property, inserted_id, that holds the id of the inserted document.
    # https://www.w3schools.com/python/python_mongodb_insert.asp#:~:text=The%20insert_one()%20method%20returns%20a%20InsertOneResult%20object%2C%20which%20has%20a%20property%2C%20inserted_id%2C%20that%20holds%20the%20id%20of%20the%20inserted%20document.
    print(result.inserted_id)
    return find_cat(result.inserted_id)


def update_cat(_id, name_: str, age_: str, features_: list):
    result = poland_cats.update_one(
        {"_id": ObjectId(_id)},
        {"$set": {"name": name_, "age": int(age_), "features": features_}},
    )

    return find_cat(_id)


def update_cat_name(name_: str, new_name: str):
    result = poland_cats.update_one({"name": name_}, {"$set": {"name": new_name}})
    if result.modified_count > 0:
        return find_cat(poland_cats.find_one({"name": new_name})["_id"])
    else:
        raise ExceptValidation(f"No cat with name {name_} found")
        return None


def remove_cat(_id):
    result = poland_cats.delete_one({"_id": ObjectId(_id)})
    return result


def main():
    try:
        match action:
            case "create":
                r = create_cat(name, age, features)
                pprint(r)
            case "find":
                r = find_cats()
                [pprint(cat) for cat in r]
            case "update":
                r = update_cat(_id, name, age, features)
                pprint(r)
            case "update_name":
                r = update_cat_name(name, new_name)
                pprint(r)
            case "remove":
                r = remove_cat(_id)
                pprint(r.deleted_count)
            case _:
                pprint("Unknown command")
    except ExceptValidation as err:
        pprint(err)


if __name__ == "__main__":
    main()
