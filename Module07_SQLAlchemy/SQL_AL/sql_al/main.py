import argparse
import sys
from sqlalchemy.exc import SQLAlchemyError

from database.repository import (
    get_user,
    get_all_todos,
    create_todo,
    update_todo,
    remove_todo,
)

parser = argparse.ArgumentParser(description="Todo APP")
parser.add_argument("--action", help="Command: create, update, list, remove")
parser.add_argument("--id")
parser.add_argument("--title")
parser.add_argument("--desc")
parser.add_argument("--login")

arguments = parser.parse_args()
# print(arguments)
my_arg = vars(arguments)
# print(my_arg)

action = my_arg.get("action")
title = my_arg.get("title")
description = my_arg.get("desc")
_id = my_arg.get("id")
login = my_arg.get("login")


def main(user):

    match action:
        case "create":
            create_todo(title=title, description=description, user=user)
        case "list":
            todos = get_all_todos(user)
            for t in todos:
                print(
                    t.id,
                    f"Author {t.user.login} | ",
                    t.title,
                    t.description,
                )
        case "update":
            t, user_name = update_todo(
                _id=_id, title=title, description=description, user=user
            )
            if t:
                print(
                    t.id,
                    f"Author {user_name} | ",  # Cannot get name of user. Why???
                    t.title,
                    t.description,
                )
            else:
                print("Not found!!!")
        case "delete":
            r = remove_todo(_id=_id, user=user)
            print(f"Removing: {r}")
        case _:
            print("Nothing")


if __name__ == "__main__":
    user = get_user(login)
    password = input("Password: ")
    if password == user.password:
        main(user)
    else:
        print(f"Incorrect password")
    print(f"ACTION WAS - {action}")
