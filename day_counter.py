import datetime

today = datetime.date.today()


def get_birthday_date(date):
    dt_object = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')
    date_object = dt_object.date()
    return date_object


def replace_year(date, year):
    try:
        date = date.replace(year=year)
    except ValueError:
        date = date.replace(year=year, month=date.month + 1, day=1)

    return date


def it_is_this_year(date):
    if (today.month, today.day) < (date.month, date.day):
        return True
    else:
        return False


def days_between(date):
    birthday = get_birthday_date(date)
    birthday = replace_year(birthday, today.year)

    if it_is_this_year(birthday):
        return (birthday - today).days
    else:
        birthday = replace_year(birthday, birthday.year + 1)
        return (birthday - today).days
