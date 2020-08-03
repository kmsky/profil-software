from peewee import *
import json_service

parsed_json = json_service.get_json()

database = SqliteDatabase("persons.db")


class BaseModel(Model):
    class Meta:
        database = database


class Users(BaseModel):
    gender = CharField()

    name_title = CharField()
    name_first = CharField()
    name_last = CharField()

    location_street_number = CharField()
    location_street_name = CharField()
    location_city = CharField()
    location_state = CharField()
    location_country = CharField()
    location_postcode = CharField()
    location_coord_latitude = CharField()
    location_coord_longitude = CharField()
    location_timezone_offset = CharField()
    location_timezone_description = CharField()

    email = CharField()

    login_uuid = CharField()
    login_username = CharField()
    login_password = CharField()
    login_salt = CharField()
    login_md5 = CharField()
    login_sha1 = CharField()
    login_sha256 = CharField()

    dob_date = CharField()
    dob_age = CharField()
    dob_untilbirthday = CharField()

    registered_date = CharField()
    registered_age = CharField()

    phone = CharField()
    cell = CharField()

    id_name = CharField(null=True)
    id_value = CharField(null=True)

    nat = CharField()


def create_table():
    database.create_tables([Users])


def delete_table():
    database.drop_tables([Users])


def insert_db(json):
    for p in json['results']:
        table = Users(gender=p['gender'],

                      name_title=p['name']['title'],
                      name_first=p['name']['first'],
                      name_last=p['name']['last'],

                      location_street_number=p['location']['street']['number'],
                      location_street_name=p['location']['street']['name'],
                      location_city=p['location']['city'],
                      location_state=p['location']['state'],
                      location_country=p['location']['country'],
                      location_postcode=p['location']['postcode'],
                      location_coord_latitude=p['location']['coordinates']['latitude'],
                      location_coord_longitude=p['location']['coordinates']['longitude'],
                      location_timezone_offset=p['location']['timezone']['offset'],
                      location_timezone_description=p['location']['timezone']['description'],
                      email=p['email'],

                      login_uuid=p['login']['uuid'],
                      login_username=p['login']['username'],
                      login_password=p['login']['password'],
                      login_salt=p['login']['salt'],
                      login_md5=p['login']['md5'],
                      login_sha1=p['login']['sha1'],
                      login_sha256=p['login']['sha256'],

                      dob_date=p['dob']['date'],
                      dob_age=p['dob']['age'],
                      dob_untilbirthday=p['dob']['untilbirthday'],
                      registered_date=p['registered']['date'],
                      registered_age=p['registered']['age'],

                      phone=p['phone'],
                      cell=p['cell'],

                      id_name=p['id']['name'],
                      id_value=p['id']['value'],

                      nat=p['nat'])
        table.save()


if __name__ == "__main__":
    file = json_service.get_json()

    delete_table()
    create_table()
    insert_db(file)
