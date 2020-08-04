import re


class PassRating:
    def __init__(self, password):
        self.password = password


    def count_points(self):
        points = 0

        if self._has_lowercase_letter():
            points += 1

        if self._has_capital_letter():
            points += 2

        if self._has_digit():
            points += 1

        if self._is_longer_than_8():
            points += 5

        if self._has_special_char():
            points += 3

        return points


    def _has_lowercase_letter(self):
        return re.search('[a-z]', self.password)


    def _has_capital_letter(self):
        return re.search('[A-Z]', self.password)


    def _has_digit(self):
        return re.search('\d', self.password)


    def _is_longer_than_8(self):
        return len(self.password) >= 8


    def _has_special_char(self):
        return re.search('[^0-9a-zA-Z *]', self.password)
