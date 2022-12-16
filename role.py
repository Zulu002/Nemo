import json

def get_json(mainkey, key):
    with open('json/role.json', 'r', encoding='utf-8') as file:
        Badjson = file.read()
        file.close()
    GoodJson = json.loads(Badjson)[mainkey]
    return GoodJson[0].get(key)
print(get_json("Admin", "setrole"))