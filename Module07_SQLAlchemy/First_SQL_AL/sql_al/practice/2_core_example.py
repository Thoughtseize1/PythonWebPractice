# CORE
from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    ForeignKey,
    MetaData,
)

from sqlalchemy.sql import select

engine = create_engine("sqlite:///:memory:", echo=False)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("fullname", String),
)

addresses = Table(
    "addressed",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String(150), nullable=False),
    Column("user_id", Integer, ForeignKey("users.id")),
)

metadata.create_all(engine)

if __name__ == "__main__":
    with engine.connect() as conn:
        r_user = users.insert().values(fullname="Nikita Sherstianykh")
        print(r_user)
        result_user = conn.execute(r_user)

        u = conn.execute(select(users))
        print(u.fetchone())

        r_address = addresses.insert().values(
            email="n.sherstianykh@gmail.com", user_id=result_user.lastrowid
        )
        conn.execute(r_address)

        a = conn.execute(select(addresses))
        print(a.fetchone())

        a_with_u = (
            select(addresses.c.email, users.c.fullname)
            .select_from(addresses)
            .join(users)
        )
        result_1 = conn.execute(a_with_u)
        print(result_1.fetchall())
