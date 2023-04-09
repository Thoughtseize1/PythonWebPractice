from sqlalchemy import and_
from database.db import session
from database.models import User, Todo


def get_user(login):
    user = session.query(User).filter(User.login == login).first()
    return user


def create_todo(title, description, user):
    todo = Todo(title=title, description=description, user=user)
    session.add(todo)
    session.commit()
    session.close()


def get_all_todos(user):
    todos = (
        session.query(Todo).join(User).filter(Todo.user == user).all()
    )  # Filter == where session.query(Todo).join(User).where(Todo.user == user).all()
    return todos


def update_todo(_id, title, description, user):
    todo = session.query(Todo).filter(and_(Todo.user == user, Todo.id == _id)).first()
    if todo:
        todo.title = title
        todo.description = description
        session.commit()
        session.refresh(todo)
        user_name = todo.user.login
    session.close()
    return todo, user_name


###One more working case which i left here for myself
# def update_todo(_id, title, description, user):
#     todo = session.query(Todo).filter(and_(Todo.user == user, Todo.id == _id))
#     if todo:
#         todo.update({"title": title, "description": description})
#         session.commit()
#     session.close()
#     return todo.first()


def remove_todo(_id, user):
    r = session.query(Todo).filter(and_(Todo.user == user, Todo.id == _id)).delete()
    session.commit()
    session.close()
    return r
