from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey


metadata = MetaData()
engine = create_engine("sqlite:///:memory:", echo=True)

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("fullname", String),
)

addresses = Table(
    "addresses",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("email_address", String, nullable=False),
)

metadata.create_all(engine)

ins = users.insert().values(name="jack", fullname="Jack Jones")
print(str(ins))  # INSERT INTO users (name, fullname) VALUES (:name, :fullname)
