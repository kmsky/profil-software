import json_service
import json_to_sqlite

if __name__ == "__main__":
    json = json_service
    db = json_to_sqlite

    json.add_days_until_birthday()
    json.sanitize_phone_number()
    json.delete_picture()

    db = json_to_sqlite
    db.json_to_db()