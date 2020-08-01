import re

def delete_special_char(number):
    return re.sub('[^A-Za-z0-9]+', '', number)