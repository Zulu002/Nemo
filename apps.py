import psycopg2

import config as setting


class Db:
    def __init__(self):
        self.connection = psycopg2.connect(user=setting.USER,
                                           password=setting.PASSWORD,
                                           host=setting.HOST,
                                           port=setting.PORT,
                                           database=setting.DB_NAME)
        self.connection.autocommit = True
        self.cur = self.connection.cursor()

    def insert_user(self, id, phone, site):

        self.cur.execute(
            """INSERT INTO users (id, phone, site) VALUES (%s, %s, %s)"""
            , (id, phone, site))
        return True

    # def insert_memders(self):
Db().insert_user(132, 73112331, 'vk')
