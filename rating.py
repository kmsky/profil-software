import db_service
import re

users = db_service.Users


def count_points(password):
    points = 0

    if has_lowercase_letter(password):
        points += 1

    if has_capital_letter(password):
        points += 2

    if has_digit(password):
        points += 1

    if is_longer_than_8(password):
        points += 5

    if has_special_char(password):
        points += 3

    return points


def has_lowercase_letter(text):
    return re.search('[a-z]', text)


def has_capital_letter(text):
    return re.search('[A-Z]', text)


def has_digit(text):
    return re.search('\d', text)


def is_longer_than_8(text):
    return len(text) >= 8


def has_special_char(text):
    return re.search('[^0-9a-zA-Z *]', text)


if __name__ == "__main__":
    count_points("Supertajne1$")
