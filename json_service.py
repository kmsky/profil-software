import json
from day_counter import DayCounter
import phone_nr


class JSONService:

    def __init__(self):
        with open('persons.json', 'r', encoding="utf8") as file:
            self.parsed_json = json.load(file)

    def print_json(self):
        print(json.dumps(self.parsed_json, indent=4, sort_keys=True))

    def add_days_until_birthday(self):
        for person in self.parsed_json["results"]:
            date = DayCounter(person['dob']['date'])
            until_birthday = date.days_between()
            person['dob']['untilBirthday'] = until_birthday

    def sanitize_phone_number(self):
        for person in self.parsed_json["results"]:
            person["cell"] = phone_nr.delete_special_char(person["cell"])
            person["phone"] = phone_nr.delete_special_char(person["phone"])

    def delete_picture(self):
        for person in self.parsed_json["results"]:
            person.pop("picture")


