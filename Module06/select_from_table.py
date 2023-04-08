from pprint import pprint

from db_connection import connection

simple_select = """
    SELECT * FROM users WHERE id=%s
"""


hard_select_without_id = """
    SELECT name, email, age
    FROM users
    WHERE age > 33
    ORDER BY name, age
    LIMIT 10;
"""

hard_select_with_id = """
    SELECT name, email, age
    FROM users
    WHERE age > 33
    ORDER BY name, age
    LIMIT 10;
"""

select_regex = """
    SELECT name, email, age
    FROM users
    WHERE name SIMILAR TO '%(лій|ко)%'
    ORDER BY name, age
    LIMIT 10;
"""


if __name__ == '__main__':
    with connection() as conn:
        cursor = conn.cursor()
        # cursor.execute(simple_select, (1,))
        # print(cursor.fetchone())
        cursor.execute(select_regex)
        pprint(cursor.fetchall())
        cursor.close()
