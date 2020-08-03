import json_service
import db_service

if __name__ == "__main__":
    json = json_service
    db = db_service

    json.add_days_until_birthday()
    json.sanitize_phone_number()
    json.delete_picture()
    edited_json = json.get_json()

    db.delete_table()
    db.create_table()
    db.insert_db(edited_json)