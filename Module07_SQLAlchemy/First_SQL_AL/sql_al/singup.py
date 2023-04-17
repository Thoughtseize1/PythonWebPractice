from database.db import session
from sqlalchemy.exc import SQLAlchemyError
from database.models import User

if __name__ == "__main__":
    login = input("Login: ")
    password = input("Password: ")
    try:
        user = User(login=login, password=password)
        session.add(user)
        session.commit()
    except SQLAlchemyError as err:
        session.rollback()
        print(f"ERROR - {err}")
    finally:
        session.close()
