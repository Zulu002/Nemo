
def get_users(who, id):
    with open(f"D:/formula/users/{who}.json", 'r', encoding='utf-8') as file:
        users_badjson = file.read()
        file.close()
        return json.loads(users_badjson)[id]