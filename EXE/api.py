import requests
class API:
    def __init__(self):
        self.adr = "http://192.168.1.92:2212"

    def auth(self, login, password):
        params = {"login": login, "password": password}
        result = requests.get(self.adr+'/api/v1/auth/', params=params)
        if result.status_code == 200:
            return result.json()
        return False

    def get_now_answer(self):
        return requests.get(self.adr + '/api/v1/answer/').json()

    def get_user_message(self, id):
        return requests.get(self.adr + '/api/v1/answer/'+id).json()