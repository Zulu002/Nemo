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
        def reg(login, password, email):
            cursor.execute(
                f"""INSERT INTO users (login, password, email) VALUES
                ('{login}', '{password}', '{email}');"""
            )
            return True
        print(reg('dsada', 'daas', 'yhyhyhyh'))

    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT * FROM users;"""
        )

        a = cursor.fetchone()
        print(a)

except Exception as ex:
    print("it's not work!", ex)
finally:
    if connection:
        connection.close()
        print("connect close!")