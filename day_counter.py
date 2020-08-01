import datetime


class DayCounter:
    def __init__(self, date_):
        self.date = date_
        self.today = datetime.date.today()

    def get_birthday_date(self):
        dt_object = datetime.datetime.strptime(self.date, '%Y-%m-%dT%H:%M:%S.%fZ')
        date_object = dt_object.date()
        birthday = self.replace_year(date_object, self.today.year)
        return birthday

    def replace_year(self, date, year):
        try:
            date = date.replace(year=year)
        except ValueError:
            date = date.replace(year=year, month=date.month + 1, day=1)

        return date

    def is_this_year(self, date):
        if (self.today.month, self.today.day) < (date.month, date.day):
            return True
        else:
            return False

    def days_between(self):
        birthday = self.get_birthday_date()

        if self.is_this_year(birthday):
            return (birthday - self.today).days
        else:
            birthday = self.replace_year(birthday, birthday.year+1)
            return (birthday - self.today).days
