import re
from db_creator import Users


class PassRating:
    def __init__(self):
        self.query = Users.select(Users.login_password)
        self.best_score = -1
        self.best_password = ''


    def get_best_password(self):
        return self.best_password


    def count_points(self, text):
        points = 0

        if self._has_lowercase_letter(text):
            points += 1

        if self._has_capital_letter(text):
            points += 2

        if self._has_digit(text):
            points += 1

        if self._is_longer_than_8(text):
            points += 5

        if self._has_special_char(text):
            points += 3

        return points


    def _has_lowercase_letter(self, text):
        return re.search('[a-z]', text)


    def _has_capital_letter(self, text):
        return re.search('[A-Z]', text)


    def _has_digit(self, text):
        return re.search('\d', text)


    def _is_longer_than_8(self, text):
        return len(text) >= 8


    def _has_special_char(self, text):
        return re.search('[^0-9a-zA-Z *]', text)


    def compare_score(self, new_score, password):
        if new_score > self.best_score:
            self.best_score = new_score
            self.best_password = password


    def rate_passwords(self):
        for row in self.query:
            password = row.login_password

            points = self.count_points(password)

            self.compare_score(points, password)