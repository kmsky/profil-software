import re
from day_counter import DayCounter


class JSONEditor:
    def __init__(self, json_data):
        self.json_data = json_data
        self.results = self.json_data["results"]


    def get_json(self):
        return self.json_data


    def add_days_until_birthday(self):

        for person in self.results:
            d_counter = DayCounter(person['dob']['date'])

            until_birthday = d_counter.days_until_birthday()
            person['dob']['untilbirthday'] = until_birthday


    def sanitize_phone_number(self):
        for person in self.results:
            person['cell'] = self._delete_special_char(person['cell'])
            person['phone'] = self._delete_special_char(person['phone'])


    def delete_picture(self):
        for person in self.results:
            person.pop('picture')


    @staticmethod
    def _delete_special_char(number):
        return re.sub('[^A-Za-z0-9]+', '', number)