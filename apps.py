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

    def insert_members(self, id, password, role):
        self.cur.execute(
            """INSERT INTO members (id, password, role) VALUES (%s, %s, %s)"""
            , (id, password, role))
        return True

    def insert_message(self, id, text, question):
        self.cur.execute(
            """INSERT INTO message (id, text, question) VALUES (%s, %s, %s)"""
            , (id, text, question))
        return True


Db().insert_user(132, 73111, 'vk')
Db().insert_members(1, '12345', 'admin')
Db().insert_message(1, 'hello', 'help')
