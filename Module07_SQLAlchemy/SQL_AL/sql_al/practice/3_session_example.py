# SESSION
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
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

engine = create_engine("sqlite:///:memory:", echo=False)

DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    fullname = Column(String)


class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship(User)


Base.metadata.create_all(engine)

if __name__ == "__main__":
    new_user = User(fullname="Nikita Chuvachok")
    session.add(new_user)
    new_address = Address(email="n.n@gmail.com", user=new_user)
    session.add(new_address)
    session.commit()

    u = session.query(User).one()
    print(u.id, u.fullname)

    ad = session.query(Address).one()
    print(f"Email: {ad.email} , Name = {ad.user.fullname}")

    adrs = session.query(Address).join(Address.user).all()
    for a in adrs:
        print(a.id, a.email, a.user.fullname)

    session.close()
