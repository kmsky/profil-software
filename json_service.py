import json
import re
import day_counter

with open('persons.json', 'r', encoding='utf8') as file:
    parsed_json = json.load(file)


def print_json():
    print(json.dumps(parsed_json, indent=4, sort_keys=True))


def get_single_user():
    return [user for user in parsed_json['results']]


def add_days_until_birthday():
    date = day_counter
    for person in parsed_json['results']:
        until_birthday = date.days_between(person['dob']['date'])
        person['dob']['untilBirthday'] = until_birthday


def delete_special_char(number):
    return re.sub('[^A-Za-z0-9]+', '', number)


def sanitize_phone_number():
    for person in parsed_json['results']:
        person['cell'] = delete_special_char(person['cell'])
        person['phone'] = delete_special_char(person['phone'])


def delete_picture():
    for person in parsed_json['results']:
        person.pop('picture')




if __name__ == "__main__":
    add_days_until_birthday()
    sanitize_phone_number()
    delete_picture()
    print_json()
