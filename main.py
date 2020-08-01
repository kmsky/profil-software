from json_service import JSONService

if __name__ == "__main__":
    service = JSONService()
    service.add_days_until_birthday()
    service.sanitize_phone_number()
    service.delete_picture()
    service.print_json()