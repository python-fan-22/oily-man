import json


def get_token():
    with open("token.json") as file:
        data = json.load(file)
        token = data["token"]
        return token
