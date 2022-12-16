import json

def get_user_json(mainkey, key):
    with open('json/role.json', 'r', encoding='utf-8') as file:
        Badjson = file.read()
        file.close()
    GoodJson = json.loads(Badjson)[mainkey]
    return GoodJson[0].get(key)

def get_question_json(key):
    return key