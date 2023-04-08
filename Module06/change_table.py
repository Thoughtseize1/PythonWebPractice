from faker import Faker
from pprint import pprint
from random import randint

from db_connection import connection

simple_select = """
    SELECT * FROM users WHERE id=%s
"""


change_table_users = """
    ALTER TABLE users ADD COLUMN mobilephone VARCHAR(20)
"""

my_faker = Faker('uk-UA')


if __name__ == '__main__':
    with connection() as conn:
        cursor = conn.cursor()
        cursor.execute(change_table_users)
        cursor.close()
