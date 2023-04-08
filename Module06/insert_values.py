from psycopg2 import Error
from faker import Faker
from random import randint

from db_connection import connection

insert_users = """
    INSERT INTO users(name, email,password, age)
    VALUES(%s,%s,%s,%s);
"""

my_faker = Faker('uk-UA')


def insert_1(instruction):
    with connection() as conn:
        cursor = conn.cursor()
        cursor.execute(instruction, ("Nikita", "n.sher@gmail.com", "La_laLA", 28))
        cursor.close()


def insert_2(instruction):
    with connection() as conn:
        cursor = conn.cursor()
        cursor.execute(instruction, ("Nikita", "n.sher@gmail.com", "La_laLA", 28))
        cursor.close()


if __name__ == '__main__':
    with connection() as conn:
        cursor = conn.cursor()
        for _ in range(120):
            cursor.execute(insert_users, (my_faker.name(), my_faker.email(), my_faker.password(), randint(18, 45)))
        cursor.close()
