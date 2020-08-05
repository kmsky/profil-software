import datetime


class DayCounter:

    def __init__(self, date):
        self.date = date
        self.birthday = None
        self.today = datetime.date.today()


    @staticmethod
    def _replace_year(date, year):
        try:
            date = date.replace(year=year)
        except ValueError:
            # leap year
            date = date.replace(year=year, month=date.month + 1, day=1)

        return date


    def _convert_birthday_date(self):
        dt_object = datetime.datetime.strptime(self.date, '%Y-%m-%dT%H:%M:%S.%fZ')
        date_object = dt_object.date()

        self.birthday = self._replace_year(date_object, self.today.year)


    def _birthday_already_was(self):
        if (self.today.month, self.today.day) > (self.birthday.month, self.birthday.day):
            return True
        else:
            return False


    def days_until_birthday(self):
        self._convert_birthday_date()

        if self._birthday_already_was():

            birthday_next_year = self._replace_year(self.birthday, self.birthday.year + 1)
            difference = birthday_next_year - self.today

            return difference.days

        else:

            difference = self.birthday - self.today
            return difference.days
