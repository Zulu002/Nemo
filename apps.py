import psycopg2
import config as cf
from psycopg2 import Error


try:
    connection = psycopg2.connect(
        host=cf.HOST,
        user=cf.USER,
        password=cf.PASSWORD,
        port=cf.PORT,
        database=cf.DB_NAME
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")

    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO users (login, password, email, role) VALUES
            ('DianaNice', '12345', 'hlinakcurbag', 'role1');"""
        )

        print("data in baza!")

    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT * FROM users; """
        )

        print(cursor.fetchone())

except Exception as ex:
    print("it's not work!", ex)
finally:
    if connection:
        connection.close()
        print("connect close!")