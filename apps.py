import psycopg2
import psycopg2.extras

import config as setting


class Db:
    def __init__(self):
        self.connection = psycopg2.connect(user=setting.USER,
                                           password=setting.PASSWORD,
                                           host=setting.HOST,
                                           port=setting.PORT,
                                           database=setting.DB_NAME)
        self.connection.autocommit = True
        self.cur = self.connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


    # Здесь мы передаём информацию о пользователе/админах/сообщениях от пользователя
    def insert_user(self, id, phone, site):
        self.cur.execute(
            """INSERT INTO users (id, phone, site) VALUES (%s, %s, %s);""",
            (id, phone, site,)
        )
        return True

    def insert_members(self, id, password, role):
        self.cur.execute(
            """INSERT INTO members (id, password, role) VALUES (%s, %s, %s);""",
            (id, password, role,)
        )
        return True

    def insert_message(self, id_user, platform: str) -> dict:


        self.cur.execute(
            """INSERT INTO message (id, question, datetime) VALUES (%s, %s, %s);""",
            (id, question, datetime,)
        )
        return True

    def insert_message_from_members(self, id_members, id_user, text, datetime):
        self.cur.execute(
            """INSERT INTO message_from_members (id_members, id_user, text, datetime) VALUES (%s, %s, %s, %s);""",
            (id_members, id_user, text, datetime,)
        )
        return True


    # Здесь мы можем удалить информацию о пользователе/админах/сообщениях от пользователя
    def delete_user(self, id):
        self.cur.execute(
            """DELETE FROM users WHERE id=%s;""",
            (id,)
        )
        return True

    def delete_members(self, id):
        self.cur.execute(
            """DELETE FROM members WHERE id=%s;""",
            (id,)
        )
        return True

    def delete_message(self, id):
        self.cur.execute(
            """DELETE FROM message WHERE id=%s;""",
            (id,)
        )
        return True

    def delete_message_from_members(self, id_members):
        self.cur.execute(
            """DELETE FROM message_from_members WHERE id_members=%s;""",
            (id_members,)
        )
        return True

        # вывод информации по нужной из таблиц

    def select_user_platform(self, platform, user_id):
        self.cur.execute("""SELECT * FROM users WHERE site=%s AND id_user=%s""", (platform, user_id,))
        return dict(self.cur.fetchone())

    # вывод информации по нужной из таблиц
    def select_all_users(self):
        self.cur.execute(
            """SELECT * FROM users"""
        )
        return self.cur.fetchall()

    def select_all_members(self):
        self.cur.execute(
            """SELECT * FROM members"""
        )
        return self.cur.fetchall()

    def select_all_message(self):
        self.cur.execute(
            """SELECT * FROM message"""
        )
        return self.cur.fetchall()

    def select_all_message_from_members(self):
        self.cur.execute(
            """SELECT * FROM message_from_members"""
        )
        return self.cur.fetchall()

    # def update_users(self, id, phone, site):
    #     self.cur.execute("UPDATE public.users SET id =?, phone =?, site =? WHERE ;")

# Db().insert_user(id='13fsa32', phone=None, site='vk')
# Db().insert_members(12, '12345', 'admin')
# Db().insert_message(11, 'help')
# Db().delete_user(id=912824014)
# print(Db().select_all_members())
# print(Db().select_all_message())
# print(Db().select_all_users())
# Db().update_user('87878777', '1332', 'vk')
