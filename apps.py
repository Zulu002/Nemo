import psycopg2

import config as setting


class Db:
    # Здесь мы передаём информацию о пользователе/админах/сообщениях от пользователя
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
            """INSERT INTO users (id, phone, site) VALUES (%s, %s, %s);"""
            , (id, phone, site,)
        )
        return True

    def insert_members(self, id, password, role):
        self.cur.execute(
            """INSERT INTO members (id, password, role) VALUES (%s, %s, %s);"""
            , (id, password, role,)
        )
        return True

    def insert_message(self, id, question):
        self.cur.execute(
            """INSERT INTO message (id, question) VALUES (%s, %s);"""
            , (id, question,)
        )
        return True


    # Здесь мы можем удалить информацию о пользователе/админах/сообщениях от пользователя
    def delete_user(self, id):
        self.cur.execute(
            """DELETE FROM users WHERE id=%s;""",
            (id,)
        )
        return True



Db().insert_user(id='13fsa32', phone=None, site='vk')
# Db().insert_members(12, '12345', 'admin')
# Db().insert_message(11, 'help')
# Db().delete_user(id=912824014)