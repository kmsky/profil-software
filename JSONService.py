import json


class JSONService:

    def __init__(self):
        with open('persons.json', 'r', encoding="utf8") as file:
            self.parsed_json = json.load(file)

    def print_json(self):
        print(json.dumps(self.parsed_json, indent=4, sort_keys=True))

    def add_field(self):
        for person in self.parsed_json["results"]:
            print(person['dob']['date'])

   # def day_counter(self, date):