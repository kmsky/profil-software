import requests
import json

# Project uses randomuser.me API
# https://randomuser.me/


class JSONCreator:

    def __init__(self, number_of_users):
        self.number_of_users = number_of_users

    def get_json(self):
        html = "https://randomuser.me/api/?results=" + str(self.number_of_users)
        data = requests.get(html).content

        parsed = self.parse_json(data)
        return parsed

    @staticmethod
    def parse_json(data):
        return json.loads(data)