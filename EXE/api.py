import json

import requests


class API:
    def __init__(self):
        self.adr = "http://192.168.1.92:2212"

    def auth(self, login, password):
        params = {"login": login, "password": password}
        result = requests.get(self.adr + '/api/v1/auth/', params=params)
        if result.status_code == 200:
            return result.json()
        return False

    def get_now_answer(self):
        return requests.get(self.adr + '/api/v1/answer/').json()

    def get_user_message(self, id):
        return requests.get(self.adr + '/api/v1/answer/' + id).json()

    def send_message_user(self, operator_id: int, user_id: int, msg: str):
        params = {'operator': operator_id, "id": user_id, 'msg': msg}
        return requests.post(self.adr + "/api/v1/message/", params=params)

    def close_quest(self, user_id: str):
        return requests.put(self.adr + "/api/v1/answer/"+str(user_id))

    def new_user(self, login: str, password: str, role):
        data = {"login": login, "password": password, 'role': role}
        return requests.post(self.adr + "/api/v1/auth/", data=json.dumps(data))