from models import User, TextPost, ImagePost, Post, LinkPost
from bson.objectid import ObjectId
from colors import *


def delete_user_by_id(_id):
    try:
        user = User.objects.get(id=ObjectId(_id))
        print(f"{CYAN_COLOR}FOUND USER BY ID AND DELETED:{RESET_COLOR}")
        print(user.to_mongo().to_dict())
        user.delete()
    except User.DoesNotExist:
        print(f"No user with id={_id} found.")
        return None


def delete_user_by_name(name: str):
    try:
        user = User.objects.get(first_name=name.capitalize())
        print(f"{MAGENTA_COLOR}FOUND USER BY NAME AND DELETED:{RESET_COLOR}")
        print(user.to_mongo().to_dict())
        user.delete()
    except User.DoesNotExist:
        print(f"No user with name {name} found.")
        return None


if __name__ == "__main__":
    delete_user_by_name("валерій")
