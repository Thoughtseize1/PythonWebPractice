from psycopg2 import Error
from faker import Faker
from random import randint

from db_connection import connection

update_user = """
    UPDATE users SET mobilephone = %s WHERE id = %s
"""

my_faker = Faker('uk-UA')

if __name__ == '__main__':
    with connection() as conn:
        cursor = conn.cursor()
        for id_ in range(1, 241):
            cursor.execute(update_user, (my_faker.phone_number(), id_))
        cursor.close()
