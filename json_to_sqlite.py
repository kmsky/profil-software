from peewee import *
import json_service
import re

parsed_json = json_service.get_json()

database = SqliteDatabase("persons.db")


class BaseModel(Model):
    class Meta:
        database = database


class Users(BaseModel):
    gender = CharField(null=True)

    name_title = CharField(null=True)
    name_first = CharField(null=True)
    name_last = CharField(null=True)

    location_street_number = CharField(null=True)
    location_street_name = CharField(null=True)
    location_city = CharField(null=True)
    location_state = CharField(null=True)
    location_country = CharField(null=True)
    location_postcode = CharField(null=True)
    location_coord_latitude = CharField(null=True)
    location_coord_longitude = CharField(null=True)
    location_timezone_offset = CharField(null=True)
    location_timezone_description = CharField(null=True)

    email = CharField(null=True)

    login_uuid = CharField(null=True)
    login_username = CharField(null=True)
    login_password = CharField(null=True)
    login_salt = CharField(null=True)
    login_md5 = CharField(null=True)
    login_sha1 = CharField(null=True)
    login_sha256 = CharField(null=True)

    dob_date = CharField(null=True)
    dob_age = CharField(null=True)

    registered_date = CharField(null=True)
    registered_age = CharField(null=True)

    phone = CharField(null=True)
    cell = CharField(null=True)

    id_name = CharField(null=True)
    id_value = CharField(null=True)

    nat = CharField(null=True)


def create_table():
    database.create_tables([Users])


def delete_table():
    database.drop_tables([Users])


def insert_db():
    for p in parsed_json['results']:
        user = Users(gender=p['gender'],

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

                     registered_date=p['registered']['date'],
                     registered_age=p['registered']['age'],

                     phone=p['phone'],
                     cell=p['cell'],

                     id_name=p['id']['name'],
                     id_value=p['id']['value'],

                     nat=p['nat'])
        user.save()


if __name__ == "__main__":
    delete_table()
    create_table()
    insert_db()
