from psycopg2 import connect, DatabaseError
from contextlib import contextmanager


@contextmanager
def connection():
    conn = None
    try:
        conn = connect(
            host="hattie.db.elephantsql.com", user="cszbpoof", database="cszbpoof",
            password="2gWpPsRVoEUd0oVydoonHhhZ-CEIgoSJ"
        )
        yield conn
        conn.commit()
    except DatabaseError as err:
        print(err)
        conn.rollback()
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    pass
