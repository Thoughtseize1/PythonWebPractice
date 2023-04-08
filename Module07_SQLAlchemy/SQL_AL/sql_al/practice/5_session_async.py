# SESSION
import asyncio
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
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

engine = create_async_engine("sqlite+aiosqlite:///:memory:", echo=False)

AsyncDBSession = async_sessionmaker(
    bind=engine, expire_on_commit=False, class_=AsyncSession
)  # так в документации просят указывать

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


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def main():
    await init_models()
    async with AsyncDBSession() as session:
        new_user = User(fullname="Nikita New")
        session.add(new_user)
        new_address = Address(email="n.n@gmail.com", user=new_user)
        session.add(new_address)
        await session.commit()

        new_user = User(fullname="Babka PARASKA")
        session.add(new_user)
        new_address = Address(email="BABKA2000@i.ua", user=new_user)
        session.add(new_address)
        await session.commit()

        u = await session.execute(select(User))
        result_users = u.scalars().all()
        for u in result_users:
            print(f"HEY! {u.id} - {u.fullname}.")

        # Выводит одного первого пользователя таблицы
        adrs1 = await session.execute(select(Address))
        ad = adrs1.scalars().first()
        print(f"Email: {ad.email} , Name = {ad.user.fullname}")
        print("--------------------------------------")

        # Выводит Всех чуваков в таблице
        adrs = await session.execute(select(Address).join(Address.user))
        ardesses = adrs.scalars().all()
        for a in ardesses:
            print(a.id, a.email, a.user.fullname)

        await session.close()


if __name__ == "__main__":
    asyncio.run(main())
